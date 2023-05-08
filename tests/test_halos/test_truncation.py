import pytest
from pyHalo.truncation_models import truncation_models
from pyHalo.Halos.lens_cosmo import LensCosmo
from pyHalo.Cosmology.cosmology import Cosmology
import numpy.testing as npt
from pyHalo.Halos.tidal_truncation import TruncationRN, TruncationRoche
from pyHalo.truncation_models import truncation_models
from astropy.cosmology import FlatLambdaCDM

class TestTruncation(object):

    def setup_method(self):

        astropy = FlatLambdaCDM(70.0, 0.3)
        cosmo = Cosmology(astropy)
        self.lenscosmo = LensCosmo(0.5, 1.5, cosmo)

    def test_load_models(self):

        model_name_list = ['TRUNCATION_R50', 'TRUNCATION_RN', 'TRUNCATION_ROCHE', 'TRUNCATION_ROCHE_GILMAN2020',
                           'ADIABATIC_TIDES']
        kwargs_model_list = [{}, {'LOS_truncation_factor': 50.}, {'RocheNorm': 1.0, 'm_power': 1./3, 'RocheNu': 2.0/3.0}, {},
                             {'log_m_host': 13.0, 'z_host': 0.5}]
        for model,kwargs in zip(model_name_list, kwargs_model_list):
            mod, kw = truncation_models(model)
            kwargs.update(kw)
            kwargs['lens_cosmo'] = self.lenscosmo
            _ = mod(**kwargs)

    def test_truncation_RN(self):

        N = 200
        halo_mass = 10 ** 8
        truncation_RN = TruncationRN(self.lenscosmo, N)
        r200_kpc = truncation_RN.truncation_radius(halo_mass, 0.5)
        r200_kpc_true = self.lenscosmo.NFW_params_physical(halo_mass, 16.0, 0.5)[-1]
        npt.assert_almost_equal(r200_kpc, r200_kpc_true)

    def test_truncation_roche(self):

        norm = 1.4
        m_power = 1. / 3
        nu = 2. / 3
        r3d_subhalo = 65.0
        halo_mass = 10 ** 8
        truncation_roche = TruncationRoche(None, norm, m_power, nu)
        r200_kpc = truncation_roche.truncation_radius(halo_mass, r3d_subhalo)
        r200_kpc_true = norm * (halo_mass/10**7) ** m_power * (r3d_subhalo/50)**nu
        npt.assert_almost_equal(r200_kpc, r200_kpc_true, 3)


if __name__ == '__main__':
    pytest.main()
