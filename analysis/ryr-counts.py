#!/usr/bin/env python

import matplotlib as mpl
mpl.use('Agg')  # Set the backend to Agg
import numpy as np
import matplotlib.pyplot as plt
import os
import glob



# Set-up default properties of plotting layout:
mpl.rcdefaults()

mpl.rcParams['figure.figsize'] = (8.375, 6.5)


def gen_fig(plot_data_seeds=None, plot_data_avg=None, xmax=-1, plot_title=None, plot_legend=None, plot_file=None, show_plot=False):

  fig, (ax1,ax2) = plt.subplots(nrows=1,ncols=2,sharey='row')
  fig.suptitle((plot_legend + '\n' + plot_title),fontsize=14)

  for i in range(1, plot_data_seeds.shape[1]):
    ax1.plot(plot_data_seeds[:,0],plot_data_seeds[:,i])
  if xmax>-1:
    ax1.set_xlim(xmax=xmax)
  ax1.set_title('All seeds')
  ax1.set_xlabel('time (s)')
  ax1.set_ylabel('count (#)')

#  ax2.errorbar(plot_data_avg[:,0],plot_data_avg[:,1],yerr=plot_data_avg[:,2],label=plot_legend)
  ax2.plot(plot_data_avg[:,0],plot_data_avg[:,1],label=plot_legend)
  ax2.fill_between(plot_data_avg[:,0],(plot_data_avg[:,1]-plot_data_avg[:,2]),(plot_data_avg[:,1]+plot_data_avg[:,2]),color='gray',alpha=0.2)
  if xmax>-1:
    ax2.set_xlim(xmax=xmax)
  ax2.set_title('Mean & Stddev')
  ax2.set_xlabel(r'time (s)')

  if plot_file:
    plt.savefig(plot_file + '.pdf', dpi=600)
    plt.savefig(plot_file + '.png', dpi=300)

  if show_plot:
    plt.show()
  else:
    plt.close(fig)

data_dir = '/cnl/mcelldata/Sophie/2024'

cases = [
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_40_files','Healthy AP LTCC_40 FluoOn','hL40f'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_40d_files','Disease AP LTCC_40 FluoOn','dL40f'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_40-Fluo-off_files','Healthy AP LTCC_40 FluoOff','hL40Fo'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_40d-Fluo-off_files','Disease AP LTCC_40 FluoOff','dL40Fo'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_50_files','Healthy AP LTCC_50 FluoOn','hL50f'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_50d_files','Disease AP LTCC_50 FluoOn','dL50f'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_50-Fluo-off_files','Healthy AP LTCC_50 FluoOff','hL50Fo'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_50d-Fluo-off_files','Disease AP LTCC_50 FluoOff','dL50Fo'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_10-RyR_off_files','Healthy AP LTCC_10 RyROff','hL10fRo'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_40-RyR_off_files','Healthy AP LTCC_40 RyROff','hL40fRo'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_50-RyR_off_files','Healthy AP LTCC_50 RyROff','hL50fRo'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_50-Fluo-off_Buffer-off_files','Healthy AP LTCC FluoOff and BufferOff','hL50FoBo'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_50d-Fluo-off_Buffer-off_files','Diseased AP LTCC FluoOff and BufferOff','dL50FoBo'],
#              ['Hirakis_CRU_RyR-Saftenku-deformed-LTCC_10_files','Deformed TT Healthy AP LTCC','DhL10'],
#              ['Hirakis_CRU_RyR-Saftenku-deformed-LTCC_10d_files','Deformed TT Diseased AP LTCC','DdL10'],
#              ['Hirakis_CRU_RyR-Saftenku-deformed-LTCC_40_files','Deformed TT Healthy AP LTCC','DhL40'],
#              ['Hirakis_CRU_RyR-Saftenku-deformed-LTCC_40d_files','Deformed TT Diseased AP LTCC','DdL40'],
#              ['Hirakis_CRU_RyR-Saftenku-deformed-LTCC_50_files','Deformed TT Healthy AP LTCC','DhL50'],
#              ['Hirakis_CRU_RyR-Saftenku-deformed-LTCC_50d_files','Deformed TT Diseased AP LTCC','DdL50'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_50-CSQN-jSR_files','Calsequestrin in jSR Healthy TT Healthy AP LTCC','chL50'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_50-CSQN-jSR_files','Calsequestrin in jSR Healthy TT Diseased AP LTCC','chdL50'],
#              ['Hirakis_CRU_RyR-Saftenku-healthy-LTCC_50-alt_fact-10_files','Normal TT Healthy AP LTCC 50 RyR Alt Fact 10','RyRalt10'],
#              ['Hirakis_CRU_RyR-Saftenku-healthy-LTCC_50d-alt_fact-5_files','Normal TT Diseased AP LTCC 50 RyR Alt Fact 5','RyRalt5'],
#              ['Hirakis_CRU_RyR-Saftenku-deformed-LTCC_50-alt_fact-10_files','Deformed TT Healthy AP LTCC 50 RyR Alt Fact 10','dRyRalt10'],
#              ['Hirakis_CRU_RyR-Saftenku-deformed-LTCC_50-alt_fact-5_files','Deformed TT Healthy AP LTCC 50 RyR Alt Fact 5','dRyRalt5'],
#              ['Hirakis_CRU_RyR-Saftenku-deformed-LTCC_50d-alt_fact-5_files','Deformed TT Diseased AP LTCC 50 RyR Alt Fact 5','dRyRalt5'],
#              ['Hirakis_CRU_RyR-Hake_files','Dual-state RyR model, Hake step activation','hake'],
#              ['Hirakis_CRU_RyR-Picht_files','Dual-state RyR model, Picht step activation','picht'],
#              ['Hirakis_CRU_RyR-Saftenku-healthy-LTCC_10-alt_fact-5_files','Normal TT Healthy AP LTCC 10 RyR Alt Fact 5','LTCC10RyRalt5'],
#              ['Hirakis_CRU_RyR-Saftenku-healthy-LTCC_25-alt_fact-5_files','Normal TT Healthy AP LTCC 25 RyR Alt Fact 10','LTCC25RyRalt5'],
#              ['Hirakis_CRU_RyR-Saftenku-deformed-LTCC_10-alt_fact-5_files','Deformed TT Healthy AP LTCC 10 RyR Alt Fact 5','dLTCC10RyRalt5'],
              ['Hirakis_CRU_RyR-Saftenku-deformed-LTCC_25-alt_fact-5_files','Deformed TT Healthy AP LTCC 25 RyR Alt Fact 10','dLTCC25RyRalt5'],
#              ['Hirakis_CRU_RyR-Saftenku-healthy-LTCC_50-Flux_alt_fact-10_files','Healthy AP LTCC 50 RyR Flux Alt Fact 10','RyRFlux_alt10'],
#              ['Hirakis_CRU_RyR-Saftenku-healthy-LTCC_50-Flux_alt_fact-5_files','Healthy AP LTCC 50 RyR Flux Alt Fact 5','RyRFlux_alt5'],
#              ['Hirakis_CRU_RyR-Saftenku-deformed-LTCC_50-Flux_alt_fact-10_files','Deformed TT Healthy AP LTCC 50 RyR Flux Alt Fact 10','dRyRFlux_alt10'],
#              ['Hirakis_CRU_RyR-Saftenku-deformed-LTCC_50-Flux_alt_fact-5_files','Deformed TT Healthy AP LTCC 50 RyR Flux Alt Fact 5','dRyRFlux_alt5'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_50-no_AP_files','noAP LTCC50 RyR Flux Alt Fact 5','noAP'],
#              ['Hirakis_CRU_RyR-Saftenku-healthy-LTCC_25d-alt_fact-5_files','Normal TT Disease AP LTCC 25 RyR Alt Fact 5','LTCC25RyRdalt5'],
              ['Hirakis_CRU_RyR-Saftenku-deformed-LTCC_25d-alt_fact-5_files','Deformed TT Disease AP LTCC 25 RyR Alt Fact 5','dLTCC25RyRdalt5'],
#              ['Hirakis_CRU_RyR-Saftenku-LTCC_25-RyR_off_files','Healthy AP LTCC_25 RyROff','hL25fRo'],
              ['Hirakis_Gaur_CRU_RyR-Saftenku-healthy-LTCC_25-alt_fact-5_files','25 LTCC with Gaur healthy AP','Gaur25'],
              ['Hirakis_Gaur_CRU_RyR-Saftenku-healthy-LTCC_50-alt_fact-5_files','50 LTCC with Gaur healthy AP','Gaur50'],
]





react_suffix= 'mcell/output_data/react_data'
plot_suffix= 'plots'

#   [data_file_name, data label, plot_file_prefix, xmax_value (in seconds where -1 means no limit))

react_data_files = [
                     [['RyRO1_L.World.dat','RyRO2_L.World.dat','RyRO3_L.World.dat','RyRO1_H1.World.dat','RyRO2_H1.World.dat'], 'All Open RyRs', 'OpenRyR', -1 ],
                     [['RyRC1_L.World.dat','RyRC2_L.World.dat','RyRC3_L.World.dat','RyRC4_L.World.dat','RyRC5_L.World.dat','RyRC1_H1.World.dat','RyRC2_H1.World.dat','RyRC3_H1.World.dat','RyRC4_H1.World.dat'], 'All Closed RyRs', 'ClosedRyR', -1 ],
                     [['RyRO1_L.World.dat','RyRO2_L.World.dat','RyRO3_L.World.dat'], 'All Low-gating Open RyRs', 'LowOpenRyR', -1 ],
                     [['RyRO1_H1.World.dat','RyRO2_H1.World.dat'], 'All High-gating Open RyRs', 'HighOpenRyR', -1 ],
                     [['RyRC1_L.World.dat','RyRC2_L.World.dat','RyRC3_L.World.dat','RyRC4_L.World.dat','RyRC5_L.World.dat'], 'All Low-gating Closed RyRs', 'LowClosedRyR', -1 ],
                     [['RyRC1_H1.World.dat','RyRC2_H1.World.dat','RyRC3_H1.World.dat','RyRC4_H1.World.dat'], 'All High-gating Closed RyRs', 'HighClosedRyR', -1 ],
                   ]



for case in cases:
    output_dir = os.path.join(data_dir, case[0], react_suffix)
    plot_data_dir = os.path.join(data_dir, plot_suffix)
    seed_glob = os.path.join(data_dir, case[0], react_suffix, 'seed_*')
    print('seed_glob: ' + seed_glob)
    all_seed_dirs = sorted(glob.glob(seed_glob))

    for react_data_file_list in react_data_files:
        data = []

        for seed_dir in all_seed_dirs:
            sum_data = []

            for dat_file in react_data_file_list[0]:
                file_path = os.path.join(seed_dir, dat_file)
                if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
                    print('Skipping empty file: %s' % file_path)
                    continue  # Skip empty file

                d = np.fromfile(file_path, sep=' ').reshape((-1, 2))
                if len(d) < 30000:
                    print('Skipping file (too short): %s' % file_path)
                    continue  # Skip files that are too short

                d = d[:30000, :]  # Read only up to the 30000th index

                if len(sum_data) == 0:
                    sum_data = d
                else:
                    sum_data[:, 1] += d[:, 1]  # Add second column of d to second column of sum_data

            if len(sum_data) != 0:
                if len(data) == 0:
                    data = sum_data
                else:
                    data = np.append(data, sum_data[:, 1].reshape(-1, 1), 1)

        if len(data) > 0:
            avg = data[:, 1:].mean(axis=1).reshape(-1, 1)
            stddev = data[:, 1:].std(axis=1).reshape(-1, 1)
            outdata = data[:, 0].reshape(-1, 1)
            outdata = np.append(outdata, avg, 1)
            outdata = np.append(outdata, stddev, 1)

            fn_out = react_data_file_list[2] + '.avg_stddev.dat'
            fn_out = os.path.join(output_dir, fn_out)
            print('Writing avg & stddev data: %s' % fn_out)
            np.savetxt(fn_out, outdata, fmt='%.14g', delimiter=' ', newline='\n')

            gen_fig(plot_data_seeds=data, plot_data_avg=outdata, xmax=react_data_file_list[3], plot_title=case[1], plot_legend=react_data_file_list[1], plot_file=os.path.join(plot_data_dir, react_data_file_list[2] + '_' + case[2]), show_plot=False)
  

