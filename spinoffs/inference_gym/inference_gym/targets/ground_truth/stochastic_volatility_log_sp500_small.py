# Copyright 2020 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
r"""Ground truth values for `stochastic_volatility_log_sp500_small`.

Automatically generated using the command:

```
python -m inference_gym.tools.get_ground_truth \
  --target=stochastic_volatility_log_sp500_small \
  --stan_samples=50000
```
"""

import numpy as np

IDENTITY_LOG_VOLATILITY_MEAN = np.array([
    -8.8733405736,
    -8.881073967399999,
    -9.073473969779998,
    -9.354620309400001,
    -9.509948941980003,
    -9.595035254439999,
    -9.73535877716,
    -9.74587096516,
    -9.82309774416,
    -9.74651971124,
    -9.55477168132,
    -9.238956012100001,
    -8.850009807300001,
    -8.32491795628,
    -7.7298244822600015,
    -7.448367501140001,
    -7.306349496899999,
    -6.98725180674,
    -6.907023489560001,
    -6.666585622400001,
    -6.563983841859999,
    -6.400931128900001,
    -6.2775754702,
    -6.1017447477,
    -5.781700613980001,
    -5.6535959051799995,
    -5.473931157420001,
    -5.232433479559999,
    -5.14161940846,
    -5.122223355920001,
    -5.39258476024,
    -5.62792970564,
    -5.846401729119999,
    -5.888795914399999,
    -5.89785786174,
    -5.8020158783,
    -6.0270740812,
    -6.08606140272,
    -6.28386214948,
    -6.4426856254799985,
    -6.5681649083,
    -6.5581909178,
    -6.6583122976,
    -6.6750123100400005,
    -6.54944072238,
    -6.8616020138,
    -6.996565951299999,
    -7.220386458920001,
    -7.34495693864,
    -7.32777109334,
    -7.42924225168,
    -7.5360513713,
    -7.49230458128,
    -7.53890811512,
    -7.531851298180001,
    -7.69251793462,
    -7.9274546296,
    -7.9932550016,
    -8.03200927292,
    -8.05461413504,
    -7.9353561309,
    -8.02957664072,
    -8.015215484540002,
    -8.28230805492,
    -8.40673853508,
    -8.464030835159999,
    -8.40773389506,
    -8.333687898880001,
    -8.34935625724,
    -8.20625900992,
    -8.19486739086,
    -8.221362148879999,
    -8.194979681880001,
    -8.026834013980002,
    -8.2463375823,
    -8.38507813002,
    -8.611809648080001,
    -8.74851442642,
    -8.73147698514,
    -8.7719762211,
    -8.966727014140002,
    -9.00658548024,
    -8.952497331660002,
    -8.77647424642,
    -8.55436472924,
    -8.396726254879999,
    -8.08681594808,
    -8.045787058139998,
    -7.94257429286,
    -7.71243166352,
    -7.321332104600001,
    -7.704935289939999,
    -8.0117780516,
    -8.201209157280001,
    -8.517860974600001,
    -8.69022124292,
    -8.70680058278,
    -8.614365744259997,
    -8.433266848479999,
    -8.11843029122,
]).reshape((100,))

IDENTITY_LOG_VOLATILITY_MEAN_STANDARD_ERROR = np.array([
    0.001552323187494642,
    0.0013926324263184714,
    0.0013103013199364843,
    0.0014375165864973542,
    0.0015032445388355878,
    0.001549643788229025,
    0.0016556075721341707,
    0.0017363103541468152,
    0.0019938501149814043,
    0.0020926894138799017,
    0.0019974508228620294,
    0.0018524431353649888,
    0.001724018782327666,
    0.001429900874797678,
    0.0011040838661172765,
    0.0011596588406403855,
    0.0013474554900043249,
    0.0011045834632282506,
    0.0013018788738102971,
    0.0012863377390118114,
    0.001293227647982947,
    0.0011966381329006335,
    0.0011575643283686088,
    0.001258684893869969,
    0.0010811160485445725,
    0.001111898278343125,
    0.0012448710356213794,
    0.0011717496955548857,
    0.0011938406945359405,
    0.0011982817802643874,
    0.0012077045251251276,
    0.0012824231929925497,
    0.00142905898104745,
    0.0013115180108953667,
    0.0013293653320059886,
    0.0012212115741200178,
    0.0012907312129513207,
    0.0012277611212555,
    0.0013008659254223666,
    0.0013854692884899618,
    0.0012942386689868243,
    0.0012014324244202562,
    0.0012350859061246563,
    0.0012786856834256755,
    0.0012156154446916903,
    0.0012302007281491329,
    0.0012325170907999201,
    0.0013688744124849344,
    0.0014207970511611852,
    0.001324098065816587,
    0.0012664019938218893,
    0.001397194488672574,
    0.0012506106714636576,
    0.0011265094955663951,
    0.0012433042236626242,
    0.0012513308983475011,
    0.0013664451299075736,
    0.0013732144191596508,
    0.0012610347230284395,
    0.0013172086186877391,
    0.0011477507333033897,
    0.0012145330705824497,
    0.0010933577366119217,
    0.001447138585827099,
    0.0014462439866045722,
    0.0014664191620388867,
    0.0012637445988015585,
    0.0011624193203776858,
    0.00129848531108935,
    0.0012718595429627843,
    0.0013015055724683602,
    0.0012717225246978228,
    0.0012544326274886344,
    0.0011918076457523594,
    0.0011424921558513181,
    0.0012363485030006851,
    0.0013933936187340496,
    0.0015976832589076413,
    0.0012717816770836253,
    0.0013492639093347584,
    0.0014804333859710977,
    0.0016019027524811812,
    0.0015913036634505407,
    0.0013942358140949542,
    0.0014799669462635036,
    0.0013736117007746122,
    0.0010903500624916632,
    0.0012012976480960697,
    0.0012503187070283738,
    0.001226302193255055,
    0.0010536656553271672,
    0.0011947483894009182,
    0.0013050246019980418,
    0.0013757271290735801,
    0.0017186975920047193,
    0.001850835451914996,
    0.001794935487647617,
    0.0016806019512671988,
    0.001591795639938317,
    0.0013932623115271822,
]).reshape((100,))

IDENTITY_LOG_VOLATILITY_STANDARD_DEVIATION = np.array([
    0.7883942896908247,
    0.6707581592155326,
    0.6594290397639717,
    0.7238888422458728,
    0.7346093870816314,
    0.7217407907311835,
    0.7872017985954664,
    0.7829188855025379,
    0.8867309014501862,
    0.9107486333515284,
    0.8962203375120152,
    0.8354559501286077,
    0.7838570707138139,
    0.6724124584106372,
    0.561782315739672,
    0.5779560561642701,
    0.6334883130663533,
    0.5825038017583866,
    0.6405883623903733,
    0.6003563898282948,
    0.6298466665240854,
    0.6236791523414743,
    0.6449389696355493,
    0.6573981637306017,
    0.5914147623705175,
    0.6186554021275875,
    0.6188758199291787,
    0.5796985540204287,
    0.5780506170556018,
    0.5583106922650058,
    0.6101313698604983,
    0.6460804213490317,
    0.7000004452448387,
    0.6635755296954704,
    0.6450826315859404,
    0.5708556186477389,
    0.6346394254558391,
    0.5996884193796639,
    0.6359232098155769,
    0.6502732159920808,
    0.668973579234075,
    0.6212771177246842,
    0.6497172483741462,
    0.6397428817875402,
    0.5550184511205836,
    0.6406273693384656,
    0.6217666068980068,
    0.6712872082075425,
    0.6810379013254083,
    0.622340063616422,
    0.6432641439374791,
    0.6701279103398072,
    0.6180376320941331,
    0.6219492101881677,
    0.5917884528455905,
    0.617973938976343,
    0.6874021474865369,
    0.6713837408640286,
    0.6601525839298861,
    0.6659859905855088,
    0.5928942608040771,
    0.6265788602911617,
    0.5821938827272539,
    0.6776094016433267,
    0.6950481960873309,
    0.7034007778844767,
    0.6635883075799696,
    0.6317154085284811,
    0.6682741407810169,
    0.6095565228153066,
    0.6178067206068949,
    0.6415694297537321,
    0.6422995989238723,
    0.5615719591288677,
    0.61824293746151,
    0.6205966603438415,
    0.681366923419449,
    0.7047133371683475,
    0.6459813513537295,
    0.6376589611296286,
    0.7382127118037395,
    0.759472279643925,
    0.7599750361030426,
    0.7039731615842157,
    0.6570870015917741,
    0.6672447553017251,
    0.5858206814551213,
    0.6399584112711255,
    0.6671022086714598,
    0.6300469966548496,
    0.5144180990799809,
    0.6086587669106681,
    0.6596633112360383,
    0.655748983706467,
    0.7812329396104841,
    0.8473014355563592,
    0.8348199860853812,
    0.8013984849109356,
    0.7668500992613106,
    0.7003484652379587,
]).reshape((100,))

IDENTITY_MEAN_LOG_VOLATILITY_MEAN = np.array([
    -7.661182867498001,
]).reshape(())

IDENTITY_MEAN_LOG_VOLATILITY_MEAN_STANDARD_ERROR = np.array([
    0.006203773273164915,
]).reshape(())

IDENTITY_MEAN_LOG_VOLATILITY_STANDARD_DEVIATION = np.array([
    1.1869502068074804,
]).reshape(())

IDENTITY_PERSISTENCE_OF_VOLATILITY_MEAN = np.array([
    0.9316393021399998,
]).reshape(())

IDENTITY_PERSISTENCE_OF_VOLATILITY_MEAN_STANDARD_ERROR = np.array([
    0.00014480807389693925,
]).reshape(())

IDENTITY_PERSISTENCE_OF_VOLATILITY_STANDARD_DEVIATION = np.array([
    0.042975142142105516,
]).reshape(())

IDENTITY_WHITE_NOISE_SHOCK_SCALE_MEAN = np.array([
    0.533825742426,
]).reshape(())

IDENTITY_WHITE_NOISE_SHOCK_SCALE_MEAN_STANDARD_ERROR = np.array([
    0.0003975251462025709,
]).reshape(())

IDENTITY_WHITE_NOISE_SHOCK_SCALE_STANDARD_DEVIATION = np.array([
    0.14040332147525458,
]).reshape(())
