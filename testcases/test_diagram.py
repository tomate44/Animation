

App.setActiveDocument("Unnamed")
App.ActiveDocument=App.getDocument("Unnamed")
Gui.ActiveDocument=Gui.getDocument("Unnamed")
import Animation
Animation.createManager()

App.ActiveDocument.addObject("Part::Box","Box")
App.ActiveDocument.addObject("Part::Box","Box")
App.ActiveDocument.addObject("Part::Box","Box")
App.ActiveDocument.addObject("Part::Box","Box")
App.ActiveDocument.addObject("Part::Cone","Cone")


import Placer

s1=Placer.createPlacer("B1")
s1.target=App.ActiveDocument.Box001

s2=Placer.createPlacer("B2")
s2.target=App.ActiveDocument.Box002
s2.y="10"

s3=Placer.createPlacer("B3")
s3.target=App.ActiveDocument.Box003
s3.y="20"


import Diagram
c=Diagram.createDiagram("dia","0.200*time","0.2*(0.01*time-0.5)**2","10+time+1","-10*time")
c.source=s1
c.trafo="source.Placement.Rotation.Angle"
c.timeExpression="source.time*100"
c.graphPlacement.Base.z=10


m=App.ActiveDocument.My_Manager
m.addObject(c)




