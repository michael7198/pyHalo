import numpy as np
norm_z_dV = np.array([155489817.3525053, 155987772.367822, 156489673.54456398, 156995506.59258515, 157505259.6915349, 158018923.33546552, 158536490.63463873, 159057956.57556152, 159583318.51314574, 160112575.83102247, 160645729.72171703, 161182783.56167153, 161723742.24001318, 162268604.19711953, 162817343.78140426, 163369932.0530498, 163926342.18820158, 164486548.83001167, 165050528.3734866, 165618258.8429496, 166189719.4839154, 166764891.1932646, 167343755.95124558, 167926297.0252164, 168512498.97627047, 169102347.1861789, 169695828.33426565, 170292929.89660805, 170893640.26873878, 171497948.89052734, 172105845.70330873, 172717321.67003447, 173332368.33219513, 173950977.85119164, 174573143.24459004, 175198857.76943496, 175828115.48369852, 176460910.85445487, 177097238.72331268, 177737094.6196318, 178380474.1270581, 179027373.4247942, 179677788.97279447, 180331717.4052654, 180989157.82155898, 181650114.26642254, 182314592.02046117, 182982596.61070356, 183654133.61987773, 184329209.09119758, 185007828.98425204, 185689999.5534286, 186375727.24930826, 187065018.4394824, 187757879.85755897, 188454318.09512654, 189154339.89575166, 189857952.16044107, 190565161.57753336, 191275975.11624077, 191990399.55441877, 192708441.6860904, 193430108.43224892, 194155406.3775476, 194884342.30865604, 195616922.77805963, 196353154.22296098, 197093043.1828988, 197836595.7412565, 198583818.1086134, 199334716.22307336, 200089295.77856392, 200847562.55053693, 201609521.74094573, 202375178.60642242, 203144538.0958831, 203917604.7991818, 204694383.31839076, 205474877.6424408, 206259091.69271976, 207047029.06221446, 207838692.87135613, 208634086.18141, 209433211.49100608, 210236078.85532564, 211042712.0293175, 211853136.00070116, 212667376.0370144, 213485457.138967, 214307404.42038316, 215133243.07424843, 215962998.037357, 216796694.52027804, 217634357.4854711, 218476011.9398845, 219321683.01393512, 220171395.51474595, 221025174.51558033, 221883044.86149257, 222745031.36820826, 223611159.0212116, 224481452.41129234, 225355936.38607344, 226234635.5859109, 227117574.54276457, 228004778.00642592, 228896270.25630543, 229792075.81750277, 230692219.02972516, 231596724.0466686, 232505615.2625631, 233418916.5617513, 234336652.0341783, 235258845.61383483, 236185520.97540173, 237116702.01974532, 238052412.15178418, 238992674.90140972, 239937513.682298, 240886951.57110718, 241841011.85416862, 242799717.33665943, 243763090.86257038, 244731155.2008033, 245703932.7011612, 246681445.90438786, 247663716.88556764, 248650767.66701707, 249642620.23824868, 250639296.08334792, 251640816.85629913, 252647203.7615146, 253658477.85373944, 254674660.19816157, 255695771.2640989, 256721833.63558733, 257752880.3279405, 258788948.0954565, 259830074.1346999, 260876295.3371942, 261927649.1166341, 262984172.87377653, 264045904.0605527, 265112880.6581663, 266185140.27400416, 267262721.05503696, 268345661.19098076, 269433998.86370265, 270527772.8088961, 271627021.420681, 272731783.5792853, 273842098.28452754, 274958004.4664454, 276079541.62596345, 277206748.9688381, 278339666.1203489, 279478332.90911067, 280622789.0271127, 281773074.75406766, 282929230.1243075, 284091295.5191238, 285259311.6120506, 286433318.8681713, 287613358.3568454, 288799470.9553878, 289991697.80928606, 291190080.45054996, 292394660.12575555, 293605478.7020389, 294822577.91144454, 296045999.6690303, 297275786.37618005, 298511980.06651926, 299754623.41024804, 301003759.0031854, 302259429.53239244, 303521678.2767395, 304790548.05956125, 306066082.3564618, 307348324.63320774, 308637318.3575592, 309933107.6632522, 311235736.19077885, 312545248.21111417, 313861688.0632058, 315185100.0079596, 316515528.9874975, 317853019.5045564, 319197616.60531265, 320549365.50198483, 321908311.2431683, 323274499.573489, 324647975.8559023, 326028785.90281844, 327416975.79655075, 328812591.3644748, 330215679.14439964, 331626285.35405564, 333044456.55953693, 334470239.7066528, 335903681.3890099, 337344829.31604075, 338793735.4104637, 340250454.7995516, 341715043.35629946, 343187556.7054729, 344668051.4245528, 346156584.12174296, 347653211.7493228, 349157992.10565513, 350670982.64708394, 352192241.8187996, 353721828.18997294, 355259800.56919694, 356806218.7647196, 358361142.14250416, 359924631.094647, 361496746.2370678, 363077548.3392685, 364667099.22611445, 366265460.3345446, 367872694.05854386, 369488863.14954966, 371114030.42487246, 372748259.7967185, 374391614.87622297, 376044160.1373481, 377705960.5590112, 379377081.0917019, 381057587.82170796, 382747546.6277701, 384447024.14909303, 386156087.68739086, 387874804.41474485, 389603242.68130976, 391341470.73024744, 393089557.45432097, 394847572.57685393, 396615585.58307654, 398393667.1800564, 400181888.0757906, 401980319.5080513, 403789033.7242882, 405608102.6177796, 407437599.34892404, 409277597.19475025, 411128169.83281267, 412989392.14108396, 414861338.5192522, 416744084.6810449, 418637706.5806924, 420542280.4468948, 422457883.8591682, 424384593.86512053, 426322488.8223239, 428271647.47457117, 430232148.73190486, 432204072.9050584, 434187499.88047796, 436182510.7388418, 438189187.1301878, 440207610.75447845, 442237864.76408035, 444280032.0029428, 446334196.3835791, 448400442.5835471, 450478855.2054394, 452569520.357829, 454672523.96554273, 456787952.8857408, 458915894.94954866, 461056437.7792239, 463209670.5585188, 465375682.42134833, 467554563.28666383, 469746404.27019274, 471951296.1353707, 474169331.26471335, 476400602.13454854, 478645201.8472114, 480903224.9392834, 483174765.4416186, 485459919.06386185, 487758781.763414, 490071449.9522416, 492398021.72952247, 494738594.53520787, 497093268.21186656, 499462144.08203804, 501845323.92210615, 504242911.3511374, 506655009.4477611, 509081722.9837657, 511523157.41793627, 513979418.43431455, 516450613.63163096, 518936850.2163863, 521438236.9402599, 523954883.49115354, 526486899.6331624, 529034397.12006944, 531597487.4732121, 534176283.5982181, 536770899.6036157, 539381449.5139074, 542008049.421405, 544650815.3580768, 547309864.56554, 549985315.7735159, 552677287.4556137, 555385900.2347093, 558111274.8584368, 560853533.0948919, 563612798.5050362, 566389194.209145, 569182845.5616119, 571993878.2405586, 574822418.7398984, 577668595.6719354, 580532537.0103711, 583414373.0515786, 586314234.6292253, 589232253.190408, 592168562.5733476, 595123295.877779, 598096588.5437477, 601088576.796337, 604099397.3045146, 607129189.2235931, 610178091.156737, ])
plaw_index_z = np.array([-1.9053669695663833, -1.905394166649882, -1.9054220035882405, -1.9054504869084063, -1.9054796231625994, -1.9055094189218298, -1.9055398808465307, -1.9055710155788392, -1.9056028298436034, -1.9056353304066003, -1.90566852405046, -1.9057024176559887, -1.9057370180962385, -1.905772331777859, -1.9058083634290837, -1.9058451173590194, -1.9058825978669738, -1.9059208091381634, -1.9059597553146461, -1.9059994404892404, -1.9060398686404318, -1.9060810437327473, -1.9061229696175888, -1.9061656500872415, -1.9062090888901282, -1.9062532896449706, -1.9062982559517567, -1.9063439912982976, -1.9063904990961897, -1.9064377827184387, -1.9064858453921187, -1.9065346903200662, -1.906584320593741, -1.9066347392101852, -1.906685949132893, -1.9067379531624011, -1.9067907540687712, -1.906844354511307, -1.9068987570370841, -1.9069539641588817, -1.9070099782171046, -1.9070668015092533, -1.9071244362238982, -1.9071828844207244, -1.90724214829344, -1.9073022303259368, -1.907363133038347, -1.9074248588738811, -1.90748741015782, -1.907550789195583, -1.9076149981488468, -1.9076800391272621, -1.9077459141685373, -1.9078126251759382, -1.9078801740264941, -1.9079485624546044, -1.908017792123722, -1.9080878646302737, -1.9081587814193242, -1.9082305439028933, -1.9083031533515338, -1.9083766109453957, -1.9084509178024438, -1.908526074872146, -1.9086020830637678, -1.908678943146367, -1.9087566557787958, -1.90883522156249, -1.908914640913231, -1.90899491419918, -1.9090760416496821, -1.9091580233639447, -1.9092408593884338, -1.909324549566993, -1.9094090936882644, -1.9094944914036218, -1.909580742217385, -1.9096678455740312, -1.9097558007163504, -1.9098446068126207, -1.9099342628984954, -1.9100247678461162, -1.9101161204600898, -1.9102083193553518, -1.910301363952819, -1.9103952552001593, -1.910489994121887, -1.910585581760965, -1.9106820190567995, -1.910779306929907, -1.9108774462737728, -1.91097643788172, -1.911076282562411, -1.9111769810264114, -1.9112785339498388, -1.9113809419907086, -1.9114842056940224, -1.911588325616945, -1.9116933022241807, -1.9117991359303315, -1.911905827140908, -1.912013376135606, -1.9121217832030664, -1.9122310485452554, -1.912341172298362, -1.9124521545985276, -1.9125639954434073, -1.9126766948363445, -1.9127902526999214, -1.9129046688766478, -1.9130199432127384, -1.913136075411366, -1.9132530651728314, -1.9133709121240177, -1.913489615799327, -1.913609175733552, -1.913729591324676, -1.9138508619522299, -1.9139729869315028, -1.9140959654730971, -1.9142197967846861, -1.9143444799435565, -1.9144700139930784, -1.91459639792158, -1.914723630600771, -1.914851710896131, -1.914980637549335, -1.915110409252887, -1.9152410246534206, -1.9153724822693754, -1.915504780609694, -1.9156379180662304, -1.9157718929667156, -1.915906703602101, -1.9160423481240079, -1.916178824933306, -1.9163161337695735, -1.9164542748339806, -1.9165932483611539, -1.9167330544959578, -1.9168736934290322, -1.9170151653087069, -1.9171574702517753, -1.917300608419129, -1.9174445798718847, -1.9175893847160346, -1.9177350230232737, -1.9178814948235468, -1.9180288001911434, -1.9181769391068848, -1.9183259115847482, -1.9184757176151939, -1.9186263571370537, -1.9187778301326115, -1.9189301364987983, -1.9190832761528434, -1.9192372489995708, -1.9193920548823575, -1.919547693687152, -1.9197041652227287, -1.9198614693053384, -1.9200196057499592, -1.9201785743003752, -1.9203383747420733, -1.9204990067915981, -1.920660470160198, -1.9208227645689777, -1.9209858896582013, -1.9211498451089635, -1.921314630541692, -1.921480245558814, -1.9216466897837237, -1.9218139627494297, -1.9219820640289071, -1.9221509931427656, -1.9223207495809964, -1.9224913328656237, -1.9226627424188723, -1.922834977702069, -1.9230080381324797, -1.9231819230853824, -1.9233566319745778, -1.9235321641115513, -1.923708518841528, -1.9238856954750927, -1.9240636932714255, -1.9242425115273594, -1.924422149445963, -1.9246026062514165, -1.9247838811444686, -1.924965973265181, -1.925148881790398, -1.9253326058117606, -1.9255171444295076, -1.925702496731584, -1.9258886617361204, -1.9260756384971571, -1.92626342599208, -1.926452023194509, -1.926641429076806, -1.9268316425325622, -1.9270226625422613, -1.9272144886091673, -1.9274071206092893, -1.9276005584561327, -1.9277948019973967, -1.927989851137231, -1.92818570574205, -1.9283823656723826, -1.9285798308318707, -1.9287781010496132, -1.9289771762110166, -1.9291770561723536, -1.9293777407723551, -1.9295792299042922, -1.9297815233781963, -1.9299846210602627, -1.93018852279616, -1.9303932284048588, -1.9305987377613998, -1.9308050506637473, -1.9310121669560099, -1.9312200864728395, -1.9314288090134841, -1.9316383344331292, -1.931848662518544, -1.9320597930909882, -1.9322717259737388, -1.93248446094599, -1.9326979978427474, -1.9329123364392622, -1.933127476533647, -1.9333434179374893, -1.9335601604096524, -1.9337777037646862, -1.9339960477660385, -1.9342151921884283, -1.9344351368314845, -1.9346558814335046, -1.9348774257883512, -1.9350997696474275, -1.9353229127618563, -1.9355468549190762, -1.9357715958366295, -1.9359971352875003, -1.9362234730108436, -1.9364506087340279, -1.9366785422321051, -1.9369072732017107, -1.9371368013948014, -1.9373671265381167, -1.9375982483360956, -1.937830166548399, -1.9380628808534888, -1.9382963909812294, -1.9385306966458125, -1.9387657975305652, -1.9390016933739171, -1.9392383838417913, -1.9394758686399765, -1.939714147470011, -1.9399532199940497, -1.9401930859292282, -1.940433744928849, -1.940675196674588, -1.940917440855259, -1.9411604771118096, -1.9414043051400516, -1.9416489245806139, -1.9418943350910556, -1.9421405363474142, -1.942387527969434, -1.9426353096315985, -1.9428838809618338, -1.9431332415936071, -1.9433833911901601, -1.9436343293500569, -1.9438860557264774, -1.9441385699346443, -1.9443918715839827, -1.9446459603249406, -1.9449008357349524, -1.945156497445948, -1.9454129450604638, -1.9456701781639625, -1.9459281963941188, -1.9461869993084795, -1.946446586591811, -1.9467069580242702, -1.946968113373228, -1.9472300524636295, -1.9474927750477802, -1.947756280926471, -1.948020569893705, -1.948285641712375, -1.94855149620293, -1.9488181331217698, -1.9490855522625277, -1.9493537534233607, -1.9496227363629843, -1.9498925008976546, -1.950163046788151, -1.9504343738212648, -1.9507064817995927, -1.9509793704779856, -1.9512530396688208, -1.9515274891375476, -1.9518027186644418, -1.952078728056832, -1.9523555170660263, -1.952633085500844, -1.952911433131706, -1.9531905597327, -1.9534704651161932, -1.9537511490302768, -1.9540326112805393, -1.9543148516426783, -1.9545978698849362, -1.9548816658250245, -1.9551662392081504, -1.9554515898370073, -1.9557377174928825, -1.956024621939308, -1.9563123029972767, -1.9566007604118287, -1.9568899939823103, -1.957180003495913, -1.957470788713802, -1.9577623494545935, -1.9580546854694816, ])
z_range = np.array([0.01, 0.02060790273556231, 0.031215805471124625, 0.04182370820668694, 0.05243161094224925, 0.06303951367781155, 0.07364741641337387, 0.08425531914893618, 0.09486322188449849, 0.1054711246200608, 0.1160790273556231, 0.12668693009118542, 0.13729483282674776, 0.14790273556231007, 0.15851063829787237, 0.16911854103343468, 0.179726443768997, 0.1903343465045593, 0.2009422492401216, 0.21155015197568391, 0.22215805471124622, 0.23276595744680856, 0.24337386018237087, 0.2539817629179332, 0.2645896656534955, 0.2751975683890578, 0.2858054711246201, 0.2964133738601824, 0.30702127659574474, 0.317629179331307, 0.32823708206686936, 0.33884498480243164, 0.349452887537994, 0.3600607902735563, 0.3706686930091186, 0.3812765957446809, 0.3918844984802432, 0.40249240121580554, 0.4131003039513678, 0.42370820668693016, 0.43431610942249244, 0.44492401215805477, 0.4555319148936171, 0.4661398176291794, 0.4767477203647417, 0.487355623100304, 0.49796352583586634, 0.5085714285714286, 0.519179331306991, 0.5297872340425532, 0.5403951367781156, 0.5510030395136779, 0.5616109422492402, 0.5722188449848025, 0.5828267477203648, 0.5934346504559271, 0.6040425531914895, 0.6146504559270518, 0.625258358662614, 0.6358662613981764, 0.6464741641337387, 0.657082066869301, 0.6676899696048633, 0.6782978723404256, 0.6889057750759879, 0.6995136778115503, 0.7101215805471126, 0.7207294832826748, 0.7313373860182372, 0.7419452887537995, 0.7525531914893618, 0.7631610942249241, 0.7737689969604864, 0.7843768996960487, 0.7949848024316111, 0.8055927051671734, 0.8162006079027356, 0.826808510638298, 0.8374164133738603, 0.8480243161094226, 0.8586322188449849, 0.8692401215805472, 0.8798480243161095, 0.8904559270516719, 0.9010638297872342, 0.9116717325227964, 0.9222796352583588, 0.9328875379939211, 0.9434954407294834, 0.9541033434650458, 0.964711246200608, 0.9753191489361703, 0.9859270516717327, 0.996534954407295, 1.0071428571428571, 1.0177507598784197, 1.028358662613982, 1.0389665653495441, 1.0495744680851065, 1.0601823708206688, 1.0707902735562311, 1.0813981762917935, 1.0920060790273558, 1.1026139817629181, 1.1132218844984805, 1.1238297872340428, 1.134437689969605, 1.1450455927051673, 1.1556534954407296, 1.166261398176292, 1.1768693009118543, 1.1874772036474166, 1.198085106382979, 1.2086930091185413, 1.2193009118541036, 1.2299088145896657, 1.240516717325228, 1.2511246200607904, 1.2617325227963527, 1.272340425531915, 1.2829483282674774, 1.2935562310030397, 1.304164133738602, 1.3147720364741644, 1.3253799392097265, 1.3359878419452889, 1.3465957446808512, 1.3572036474164135, 1.3678115501519759, 1.3784194528875382, 1.3890273556231005, 1.3996352583586629, 1.4102431610942252, 1.4208510638297873, 1.4314589665653497, 1.442066869300912, 1.4526747720364743, 1.4632826747720367, 1.473890577507599, 1.4844984802431613, 1.4951063829787237, 1.505714285714286, 1.5163221884498481, 1.5269300911854105, 1.5375379939209728, 1.5481458966565351, 1.5587537993920975, 1.5693617021276598, 1.5799696048632221, 1.5905775075987845, 1.6011854103343468, 1.611793313069909, 1.6224012158054713, 1.6330091185410336, 1.643617021276596, 1.6542249240121583, 1.6648328267477206, 1.675440729483283, 1.6860486322188453, 1.6966565349544076, 1.7072644376899697, 1.717872340425532, 1.7284802431610944, 1.7390881458966567, 1.749696048632219, 1.7603039513677814, 1.7709118541033437, 1.781519756838906, 1.7921276595744684, 1.8027355623100307, 1.8133434650455929, 1.8239513677811552, 1.8345592705167175, 1.8451671732522799, 1.8557750759878422, 1.8663829787234045, 1.8769908814589669, 1.8875987841945292, 1.8982066869300915, 1.9088145896656536, 1.919422492401216, 1.9300303951367783, 1.9406382978723407, 1.951246200607903, 1.9618541033434653, 1.9724620060790277, 1.98306990881459, 1.9936778115501523, 2.0042857142857144, 2.0148936170212766, 2.025501519756839, 2.0361094224924012, 2.046717325227964, 2.057325227963526, 2.067933130699088, 2.0785410334346506, 2.0891489361702127, 2.0997568389057752, 2.1103647416413374, 2.1209726443769, 2.131580547112462, 2.1421884498480246, 2.1527963525835867, 2.163404255319149, 2.1740121580547114, 2.1846200607902735, 2.195227963525836, 2.205835866261398, 2.2164437689969607, 2.227051671732523, 2.2376595744680854, 2.2482674772036475, 2.2588753799392096, 2.269483282674772, 2.2800911854103343, 2.290699088145897, 2.301306990881459, 2.3119148936170215, 2.3225227963525836, 2.333130699088146, 2.3437386018237083, 2.3543465045592704, 2.364954407294833, 2.375562310030395, 2.3861702127659576, 2.3967781155015198, 2.4073860182370823, 2.4179939209726444, 2.428601823708207, 2.439209726443769, 2.449817629179331, 2.4604255319148938, 2.471033434650456, 2.4816413373860184, 2.4922492401215806, 2.502857142857143, 2.5134650455927052, 2.524072948328268, 2.53468085106383, 2.545288753799392, 2.5558966565349546, 2.5665045592705167, 2.5771124620060792, 2.5877203647416414, 2.598328267477204, 2.608936170212766, 2.6195440729483286, 2.6301519756838907, 2.640759878419453, 2.6513677811550154, 2.6619756838905775, 2.67258358662614, 2.683191489361702, 2.6937993920972647, 2.704407294832827, 2.7150151975683894, 2.7256231003039515, 2.7362310030395136, 2.746838905775076, 2.7574468085106383, 2.768054711246201, 2.778662613981763, 2.7892705167173255, 2.7998784194528876, 2.81048632218845, 2.8210942249240123, 2.8317021276595744, 2.842310030395137, 2.852917933130699, 2.8635258358662616, 2.8741337386018238, 2.8847416413373863, 2.8953495440729484, 2.905957446808511, 2.916565349544073, 2.927173252279635, 2.9377811550151978, 2.94838905775076, 2.9589969604863224, 2.9696048632218845, 2.980212765957447, 2.990820668693009, 3.001428571428572, 3.012036474164134, 3.022644376899696, 3.0332522796352586, 3.0438601823708207, 3.0544680851063832, 3.0650759878419453, 3.075683890577508, 3.08629179331307, 3.0968996960486326, 3.1075075987841947, 3.118115501519757, 3.1287234042553194, 3.1393313069908815, 3.149939209726444, 3.160547112462006, 3.1711550151975687, 3.181762917933131, 3.1923708206686934, 3.2029787234042555, 3.2135866261398176, 3.22419452887538, 3.2348024316109423, 3.245410334346505, 3.256018237082067, 3.2666261398176295, 3.2772340425531916, 3.287841945288754, 3.2984498480243163, 3.3090577507598784, 3.319665653495441, 3.330273556231003, 3.3408814589665656, 3.3514893617021277, 3.3620972644376903, 3.3727051671732524, 3.383313069908815, 3.393920972644377, 3.404528875379939, 3.4151367781155018, 3.425744680851064, 3.4363525835866264, 3.4469604863221885, 3.457568389057751, 3.468176291793313, 3.4787841945288758, 3.489392097264438, 3.5, ])
delta_z = 0.01060790273556231
