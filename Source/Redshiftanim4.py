# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class Redshift4(AbstractAnim):
     
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("DistributionStyles in a Cluster","").setPosition([0,2.5,0])
         p11=cvo.CVO().CreateCVO("EVEN Distribution","").setPosition([3,0,0]).setangle(-TAU/3)
         p12=cvo.CVO().CreateCVO("KEY Distribution","").setPosition([-3,0,0]).setangle(TAU/3)
         p13=cvo.CVO().CreateCVO("ALL Distribution","").setPosition([0,-2.5,0]).setangle(TAU/3)
        
         p10.cvolist.append(p11)
         
         p10.cvolist.append(p12)
         p10.cvolist.append(p13)
         
         
         self.construct1(p10,p10)
         

      
if __name__ == "__main__":
    scene = Redshift4()
    scene.render()