# ===============================================================================
# Copyright 2019 Jan Hendrickx and Gabriel Parrish
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================
import os
from numpy import *
# ============= standard library imports ========================
from eiler_SA.forwardmodeling_sa import make_params_dict, forward_model_slow_bulk

"""
A script to run the model over a series of files with differing parameters from Eiler 94 for sensitivity analysis.
The arrays from the forward model will be saved w naming conventions based on the input params .txt filename
"""

if __name__ == "__main__":

    # root path
    #root = '/Users/dcadol/Desktop/academic_docs_II/FGB_model/JohnEiler/plag_hornblende_sensitivity'
    root = '/home/dan/Documents/Eiler_94/plag_hornblende_sensitivity'

    for dir in os.listdir(root):
        print(dir)
        param_path = os.path.join(root, dir)

        save_name = dir.split('.')[0]

        fwd_model_params = make_params_dict(params=param_path)

        print('running the slow model')
        xresult, yresult, timeresult = forward_model_slow_bulk(fwd_model_params)

        # Save each array as a .npy file
        save(os.path.join(root, '{}_x.npy'.format(save_name)), xresult)
        save(os.path.join(root, '{}_y.npy'.format(save_name)), yresult)
        save(os.path.join(root, '{}_time.npy'.format(save_name)), timeresult)