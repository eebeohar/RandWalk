from random import choice
import numpy as np
import matplotlib.pyplot as plt

class RandomWalk:
    
    def __init__(self,WalkPoints=1000):
        
        self.WalkPoints = WalkPoints
        self.X = [0]
        self.Y = [0]
        self.Z = [0]
        self.problist = np.array([]) #Probability Density
    
    def Loop(self,Xbias=None, Ybias=None, Zbias=None, MaxUnit=None,dim=2):
                
        DirectionX = choice([1,-1])
        DirectionY = choice([1,-1])
        DirectionZ = choice([1,-1])
        StepLenX = 1
        StepLenY = 1
        StepLenZ = 1
                 
        if Xbias=='+Xaxis':
            StepLenX = choice(np.arange(1,MaxUnit))
            DirectionX = choice([1,-1,1])
            
        elif Xbias=='-Xaxis':
            StepLenX = choice(np.arange(1,MaxUnit))
            DirectionX = choice([-1,-1,1])
            
        elif Ybias=='-Yaxis':
            StepLenY = choice(np.arange(1,MaxUnit))
            DirectionY = choice([1,-1,-1])
        
        elif Ybias=='+Yaxis':
            StepLenY = choice(np.arange(1,MaxUnit))
            DirectionY = choice([1,-1,1])
            
            
           
        StepX = DirectionX*StepLenX
        StepY = DirectionY*StepLenY
        
      
            
        PointX = self.X[-1]+StepX
        PointY = self.Y[-1]+StepY
        self.X.append(PointX)
        self.Y.append(PointY)
        
        if dim==3:
            
            if Zbias=='+Zaxis':
                
                StepLenZ = choice(np.arange(1,MaxUnit))
                DirectionZ = choice([1,-1,1])
            
            elif Zbias=='-Zaxis':
                StepLenZ = choice(np.arange(1,MaxUnit))
                DirectionZ = choice([-1,-1,1])
            
            StepZ = DirectionZ*StepLenZ
            PointZ = self.Z[-1]+StepZ
            self.Z.append(PointZ)
    
    
    def fill_walk(self,Xbias=None, Ybias=None, Zbias=None, MaxUnit=None,dim=2):
        
        while len(self.X)<self.WalkPoints and len(self.Y)<self.WalkPoints and len(self.Z)<self.WalkPoints:
            self.Loop(Xbias,Ybias,Zbias,MaxUnit,dim)
           
        
            
    
    def Prob(self,walks,Xbias=None,Ybias=None,Zbias=None, MaxUnit=None,dim=2): 
        Start=-(self.WalkPoints)//2
        End=(self.WalkPoints)//2
        problistM = np.array([])
        problistN = np.array([])
        problistP = np.array([])
        dummyproblistM = np.array([])
        dummyproblistN = np.array([])
        dummyproblistP = np.array([])
        
        
        for m in range(Start,End):
        
            i =0
            while i < walks:
                
                self.fill_walk(Xbias,Ybias,Zbias, MaxUnit)
                probM = self.X.count(m)/len(self.X)
                dummyproblistM = np.append(dummyproblistM, probM)
                i=i+1
                
            problistM = np.append(problistM, np.mean(dummyproblistM))
      
         
        for n in range(Start,End):
            
            i=0
            while i<walks:
                
                 self.fill_walk(Xbias,Ybias,Zbias,MaxUnit)
                 probN = np.array(self.Y.count(n)/len(self.Y))
                 dummyproblistN = np.append(dummyproblistN,probN)
                 i=i+1
                 
            problistN=np.append(problistN, np.mean(dummyproblistN))
            
        self.problist = problistM*problistN
            
        if dim==3:
            
            for p in range(Start,End):
                
            
                i=0
                while i<walks:
                    
                    self.fill_walk(Xbias,Ybias,Zbias,MaxUnit,dim=3)
                    probP = np.array(self.Z.count(p)/len(self.Z))
                    dummyproblistP= np.append(dummyproblistP,probP)
                    i=i+1
                     
                problistP=np.append(problistP, np.mean(dummyproblistP))
            
            self.problist = problistM*problistN*problistP
            
            
    def PlotProb(self,dim,walks=10,Xbias=None,Ybias=None,Zbias=None, MaxUnit=None):
        
        if dim==2:
            self.Prob(walks,Xbias,Ybias, MaxUnit,dim)
            
            x_values = self.X
            y_values = self.Y
            z_values = self.problist
            c = self.problist
            
            
            plt.style.use('classic')
            fig = plt.figure(figsize = (20, 15)) 
            ax = plt.axes(projection ="3d")
            ax.scatter3D(x_values, y_values, z_values, c=c, cmap=plt.cm.Reds)
            ax.set_title('2d Walk Probability',fontsize=30)
            ax.set_xlabel('X-axis', fontsize = 20)
            ax.set_ylabel('Y-axis', fontsize = 20)
            ax.set_zlabel('Probability (x,y)', fontsize = 20)
            ax.set_zticks([])
            
            plt.show()
        
        else:
            
            self.Prob(walks,Xbias,Ybias,Zbias, MaxUnit,dim=3)
          

            x_values = self.X
            y_values = self.Y
            z_values = self.Z
            c = self.problist
            
            plt.style.use('classic')
            fig = plt.figure(figsize = (20, 15))
            ax = plt.axes(projection ="3d")
            ax.set_title('3d Walk Probability',fontsize=30)
            ax.set_xlabel('X-axis', fontsize = 10)
            ax.set_ylabel('Y-axis', fontsize = 10)
            ax.set_zlim(-50,50)
            ax.set_xlim(-50,50)
            ax.set_ylim(-50,50)
            img = ax.scatter(x_values, y_values, z_values, c=c, cmap=plt.cm.Reds)
            fig.colorbar(img)
            plt.show()
        

    def PlotWalk(self,dim=2, Xbias=None, Ybias=None, Zbias=None, MaxUnit=None,AnimateWalk=False):
        
        if dim==2:
            
            self.fill_walk( Xbias, Ybias, Zbias, MaxUnit,dim=2)
            plt.style.use('classic')
            fig, ax = plt.subplots()
            point_numbers = range(self.WalkPoints)
            ax.scatter(self.X,self.Y, c=point_numbers, cmap=plt.cm.Reds,edgecolors='none',s=15)
            ax.scatter(0, 0, c='black', edgecolors='b', s=100)
            ax.scatter(self.X[-1], self.Y[-1], c='green', edgecolors='none',s=100)
            plt.axis('off')
            plt.show()
        
        elif dim==3 and AnimateWalk==True:
            NumberOfWalks = 1
            while len(self.X)<self.WalkPoints:
                if NumberOfWalks%100==0:
                    KeepRunning = input(f'{NumberOfWalks} Walks done,Continue?')
                    if KeepRunning == 'n':
                        break
                    elif KeepRunning == 'y':
                        pass
                    
        

                self.Loop(Xbias, Ybias, Zbias, MaxUnit,dim=3)
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')            
                plt.axis('off')
                img = ax.scatter(self.X, self.Y, self.Z)                
                plt.show()
                plt.clf()
                
                NumberOfWalks = NumberOfWalks+1
                
            
        else:
            self.fill_walk( Xbias, Ybias, Zbias, MaxUnit,dim=3)
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            img = ax.scatter(self.X, self.Y, self.Z)
            ax.set_title('3d Random Walk',fontsize=20)
            plt.show()
        
        
RandomWalk().PlotWalk(dim=3, Xbias=None, Ybias=None, Zbias=None, MaxUnit=None,AnimateWalk=False)
