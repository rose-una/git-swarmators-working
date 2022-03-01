from cc3d import CompuCellSetup
from cc3d.core.PySteppables import *
from cc3d.cpp.PlayerPython import * 
from random import random
from random import uniform

import numpy as np

import math

#Phase synchronization by relative cell location (see in Contact Plugin in xml file)

#Define parameters
#K=0.001
K = {{K}}
omega = 0.001


class cellsort_2DSteppable(SteppableBasePy):

    def __init__(self,frequency=1):

        SteppableBasePy.__init__(self,frequency)
        self.cellclock=self.createScalarFieldCellLevelPy("CellClock")
        
        #Color for different valued internal clocks
        self.track_cell_level_scalar_attribute(field_name='SIN_CLOCK', attribute_name='internalclock')
        
    def start(self):
        """
        any code in the start function runs before MCS=0
        """
        for cell in self.cellList:
            self.cellclock[cell]=uniform(0,2*math.pi)
            cell.dict['internalclock'] = math.sin(3*self.cellclock[cell])
              
            
            
        ##Plot to track individual cell clocks      
        #self.plot_win = self.add_new_plot_window(title='Cell clocks',
        #                                         x_axis_title='MonteCarlo Step (MCS)',
        #                                         y_axis_title='Clock', x_scale_type='linear', y_scale_type='linear',
        #                                         grid=False)       
        #self.plot_win.add_plot("Cell #20", style='Dots', color='red', size=1)
        #self.plot_win.add_plot("Cell #21", style='Dots', color='blue', size=1)
        #self.plot_win.add_plot("Cell #22", style='Dots', color='green', size=1)
        
        
        
    def step(self,mcs): 
        """
        """
        
        for cell in self.cellList:
            self.cellclock[cell]=self.cellclock[cell]+omega
            cell.dict['internalclock'] = math.sin(3*self.cellclock[cell])
              
            for neighbor, common_surface_area in self.get_cell_neighbor_data_list(cell):
                self.cellclock[cell]=self.cellclock[cell]+omega*{{K}}*math.sin(self.cellclock[neighbor]-self.cellclock[cell])

            ## needed for Local ProductPlugin: set j-value to cellclock -->
            ## see demo CompuCell3D-py3-64bit\Demos\PluginDemos\ContactLocalProduct\ContactLocalProductExample
            self.contactLocalProductPlugin.setJVecValue(cell, 0,self.cellclock[cell])


        for cell in self.cellList:
            if cell.id==20:
                print("cell.id=",cell.id)
                print("self.cellclock[cell]=",self.cellclock[cell])   
                
        ## arguments are (name of the data series, x, y)
        #self.plot_win.add_data_point("Cell #20", mcs, self.cellclock[self.attemptFetchingCellById(20)])
        #self.plot_win.add_data_point("Cell #21", mcs, self.cellclock[self.attemptFetchingCellById(21)])
        #self.plot_win.add_data_point("Cell #22", mcs, self.cellclock[self.attemptFetchingCellById(22)])
        
        
        
    def finish(self):
        """
        Finish Function is called after the last MCS
        """


