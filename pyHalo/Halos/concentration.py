import numpy as numpy
from colossus.halo.concentration import concentration, peaks
import warnings
import numpy
from scipy.interpolate import RegularGridInterpolator

warnings.filterwarnings("ignore")

__all__ = ['ConcentrationDiemerJoyce',
           'ConcentrationWDMHyperbolic',
           'ConcentrationWDMPolynomial',
           'ConcentrationPeakHeight']

class _ConcentrationCDM(object):

    def __init__(self, cosmo, scatter=True, scatter_dex=0.2, *args, **kwargs):
        """
        This class handles concentrations of the mass-concentration relation for NFW profiles
        :param lens_cosmo: an instance of LensCosmo
        """
        self._cosmo = cosmo
        self._scatter = scatter
        self._scatter_dex = scatter_dex

    def nfw_concentration(self, m, z):
        """
        Evaluates the concentration of a halo of mass 'm' at redshift z
        :param M: halo mass [M_sun]
        :param z: halo redshift
        :return:
        """
        if isinstance(m, numpy.float) or isinstance(m, numpy.int):
            c = self._evaluate_concentration(m, z)
        else:
            c = numpy.array([self._evaluate_concentration(mi, z) for mi in m])
        if self._scatter:
            log_c = numpy.log(c)
            c = numpy.random.lognormal(log_c, self._scatter_dex)
        return c

    def _evaluate_concentration(self, *args, **kargs):
        raise Exception(
            'Custom concentration class must have a method evaluate_concentration with inputs mass, redshift')

class _ConcentrationTurnover(object):

    def __init__(self, cdm_concentration):
        """

        :param cdm_concentration: an instantiated CDM concentration-mass relation class
        """
        self._cdm_concentration = cdm_concentration

    def nfw_concentration(self, m, z):
        """
        Evaluates the concentration of a halo of mass 'm' at redshift z
        :param M: halo mass [M_sun]
        :param z: halo redshift
        :return:
        """
        c_cdm = self._cdm_concentration.nfw_concentration(m, z)
        return c_cdm * self.suppression(m, z)

    def suppression(self, *args, **kwargs):
        raise Exception('a WDM model with a turnover must have a suppression function')

class ConcentrationDiemerJoyce(_ConcentrationCDM):

    name = 'DIEMERJOYCE19'

    def __init__(self, cosmo, scatter=True, scatter_dex=0.2, mdef='200c', *args, **kwargs):
        """
        This class handles concentrations of the mass-concentration relation for NFW profiles
        :param cosmo: an instance of astropy cosmology
        """
        self._mdef = mdef
        super(ConcentrationDiemerJoyce, self).__init__(cosmo, scatter, scatter_dex)

    def _evaluate_concentration(self, M, z):

        """
        Evaluates the concentration of an NFW profile

        :param M: halo mass; m200 with respect to critical density of the Universe at redshift z
        :param z: redshift
        :return: halo concentratioon
        """
        model = 'diemer19'
        if isinstance(M, float) or isinstance(M, int):
            M_h = M * self._cosmo.h
            c = concentration(M_h, mdef=self._mdef, model=model, z=z)
        else:
            if isinstance(z, numpy.ndarray) or isinstance(z, list):
                assert len(z) == len(M)
                c = []
                for (mi, zi) in zip(M, z):
                    M_h = mi * self._cosmo.h
                    c.append(concentration(M_h, mdef=self._mdef, model=model, z=zi))
            else:
                M_h = M * self._cosmo.h
                c = concentration(M_h, mdef=self._mdef, model=model, z=z)
        return c

class ConcentrationLudlow(_ConcentrationCDM):

    name = 'LUDLOW2016'

    def __init__(self, cosmo, scatter=True, scatter_dex=0.2, mdef='200c', *args, **kwargs):
        """
        This class handles concentrations of the mass-concentration relation for NFW profiles
        :param cosmo: an instance of astropy cosmology
        """
        self._cosmo = cosmo
        self._mdef = mdef
        self._interp = self._setup_model()
        super(ConcentrationLudlow, self).__init__(cosmo, scatter, scatter_dex)

    def _setup_model(self):
        """
        As discussed in the Colossus documentation the evaluation of this model is efficient for large arrays of
        halo masses but inefficient for individual halo masses. Therefore, in this routine we will compute the m-c
        relation on a grid (efficient) and interpolate it to later sample individual conentrations
        :return:
        """
        n = 40
        log10m_array = numpy.log10(numpy.logspace(5, 11, n))
        z_array = numpy.linspace(0, 5, n)
        values = numpy.empty((n, n))
        for i in range(0, len(z_array)):
            values[:, i] = self.evaluate_concentration_colossus(10**log10m_array, z_array[i])
        points = (log10m_array, z_array)
        interp = RegularGridInterpolator(points, values)
        return interp

    def evaluate_concentration_colossus(self, m, z):
        """
        This function makes a direct call to Colossus to do the calculation of the median halo concentration.
        This is inefficient for individual halo masses
        :param m: halo mass in units 200c
        :param z: halo redshift
        :return: halo concentration
        """
        model = 'ludlow16'
        M_h = m * self._cosmo.h
        c = concentration(M_h, mdef=self._mdef, model=model, z=z)
        return c

    def _evaluate_concentration(self, M, z):

        """
        Evaluates the concentration of an NFW profile

        :param M: halo mass; m200 with respect to critical density of the Universe at redshift z
        :param z: redshift
        :return: halo concentratioon
        """
        M_h = M * self._cosmo.h
        point = (numpy.log10(M_h), z)
        c = float(self._interp(point))
        return c

class ConcentrationPeakHeight(_ConcentrationCDM):

    name = 'PEAK_HEIGHT_POWERLAW'

    def __init__(self, cosmo, c0, zeta, beta, scatter=True, scatter_dex=0.2):
        """
        This class handles concentrations of the mass-concentration relation for NFW profiles
        :param cosmo: an instance of astropy cosmology
        :param c0: the amplitude of the concentration-mass relation at 10^8 M_sun at z=0
        :param zeta: modifies the logarithmic slope of the concentration-mass relation (1+z)^zeta
        :param beta: the logarithmic slope of the concentration-mass relation in peak height
        :param scatter: bool; whether to include scatter in concentration-mass relation
        :param scatter_dex: scatter in concentration in dex
        """
        self._c0 = c0
        self._zeta = zeta
        self._beta = beta
        self._redshift_evolution = _zEvolutionPeakHeight(cosmo)
        super(ConcentrationPeakHeight, self).__init__(cosmo, scatter, scatter_dex)

    def _evaluate_concentration(self, M, z):

        """
        Evaluates the concentration of an NFW profile

        :param M: halo mass; m200 with respect to critical density of the Universe at redshift z
        :param z: redshift
        :return: halo concentratioon
        """
        M_h = M * self._cosmo.h
        Mref_h = 10 ** 8 * self._cosmo.h
        nu = peaks.peakHeight(M_h, z)
        nu_ref = peaks.peakHeight(Mref_h, z)
        redshift_factor = self._redshift_evolution(M, z)
        c = self._c0 * (nu / nu_ref) ** -self._beta * redshift_factor ** self._zeta
        return c

class ConcentrationWDMPolynomial(_ConcentrationTurnover):

    name = 'WDM_POLYNOMIAL'

    def __init__(self, cosmo, concentration_cdm_class, log_mc, c_scale=60.0,
                 c_power=-0.17, c_power_inner=1.0, mc_suppression_redshift_evolution=True, scatter=True,
                 scatter_dex=0.2, kwargs_cdm={}):
        """

        :param cosmo: an instance of astropy cosmology
        :param concentration_cdm_class: a concentration class for CDM
        :param c_scale: the leading coefficient of the suppression term (see below)
        :param c_power: the exponent outside the parenthesis of the suppression term (see equation below)
        :param c_power_inner: the exponent inside the parenthesis of the suppression term (see equation below)
        :param mc_suppression_redshift_evolution: bool; adds the (mild) redshift evolution from Bose et al. (2016)
        :param scatter: bool; whether to include scatter in concentration-mass relation
        :param scatter_dex: scatter in concentration in dex
        :param kwargs_cdm: keyword arguments for the CDM concentration class
        """
        if 'scatter' not in kwargs_cdm.keys():
            kwargs_cdm['scatter'] = scatter
        if 'scatter_dex' not in kwargs_cdm.keys():
            kwargs_cdm['scatter_dex'] = scatter_dex
        cdm_concentration = concentration_cdm_class(cosmo, **kwargs_cdm)
        if c_power > 0:
            raise Exception('c_power parameters > 0 are unphysical')
        if c_scale < 0:
            raise Exception('c_scale parameters < 0 are unphysical')
        self._log_mc = log_mc
        self._c_scale = c_scale
        self._c_power = c_power
        self._c_power_inner = c_power_inner
        self._mc_suppression_redshift_evolution = mc_suppression_redshift_evolution
        self._redshift_evolution = _zEvolutionBose2016()
        super(ConcentrationWDMPolynomial, self).__init__(cdm_concentration)

    def suppression(self, m, z):
        """

        :param m: halo mass [same units as log_mc]
        :param z: halo redshift
        :param log_mc: mass scale where suppresion kicks in [same units as m]
        :return:
        """

        mhm = 10 ** self._log_mc
        rescale_factor = (1 + self._c_scale * (mhm / m) ** self._c_power_inner) ** self._c_power
        if self._mc_suppression_redshift_evolution:
            redshift_factor = self._redshift_evolution(m, z)
        else:
            redshift_factor = 1.0
        rescale = redshift_factor * rescale_factor
        return rescale

class ConcentrationWDMHyperbolic(_ConcentrationTurnover):

    name = 'WDM_HYPERBOLIC'

    def __init__(self, cosmo, concentration_cdm_class, log_mc, a,  b, scatter=True,
                 scatter_dex=0.2, kwargs_cdm={}):
        """

        :param cosmo:
        :param concentration_cdm_class:
        :param kwargs_cdm:
        """
        if 'scatter' not in kwargs_cdm.keys():
            kwargs_cdm['scatter'] = scatter
        if 'scatter_dex' not in kwargs_cdm.keys():
            kwargs_cdm['scatter_dex'] = scatter_dex
        cdm_concentration = concentration_cdm_class(cosmo, **kwargs_cdm)
        self._a = a
        self._b = b
        self._log_mc = log_mc
        super(ConcentrationWDMHyperbolic, self).__init__(cdm_concentration)

    def suppression(self, m, z):
        """

        :param m:
        :param z:
        :param log_mc:
        :param a:
        :param b:
        :return:
        """
        mhm = 10 ** self._log_mc
        log10u = numpy.log10(m / mhm)
        argument = (log10u - self._a) / (2 * self._b)
        return 0.5 * (1 + numpy.tanh(argument))

class _zEvolutionPeakHeight(object):

    def __init__(self, cosmo):
        self._cosmo = cosmo

    def __call__(self, m, z):
        """
        This method evaluates the redshift evolution according to the redshift evolution of the peak height
        :param m: halo mass in units 200c
        :param z: redshift
        :return: the relative evolution of the peak height between z=0 and z=z
        """
        M_h = m * self._cosmo.h
        redshift_factor = peaks.peakHeight(M_h, 0.0) / peaks.peakHeight(M_h, z)
        return redshift_factor


class _zEvolutionBose2016(object):

    def __call__(self, m, z):
        """
        This method evaluates the redshift evolution according to the redshift evolution for WDM halos presented by
        Bose 2016
        :param m: halo mass in units 200c
        :param z: redshift
        :return: the scaling with redshift of the Bose et al. (2016) model
        """
        redshift_factor = (1 + z) ** (0.026 * z - 0.04)
        return redshift_factor
