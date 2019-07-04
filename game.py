import turtle
import sys
sys.path.append("C:\\Users\\new user.LAPTOP-5GLT5PL6\\Anaconda3\\Lib\\site-packages")
import numpy as np
import time
import random
from Agent import realAgent
class Environment(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.points_1=0
		self.points_2=0
		self.movedirection=0
		self.punchduration=0
		self.kickduration=0
		self.dodgeduration=0
		self.shape='steady'
		self.pshape=self.shape
		self.power=20
		self.power2=20
		self.xcor=-82
		self.rkickhold=0
		self.rkickhold2=0
		self.xcor2=82
		self.movedirection2=0
		self.punchduration2=0
		self.kickduration2=0
		self.dodgeduration2=0
		self.shape2='steady'
		self.pshape2=self.shape2
		self.screen=turtle.Screen()
		self.screen.setup(500,700)
		self.screen.tracer(0)
		self.screen.addshape('steady.gif')
		self.screen.addshape('punch.gif')
		self.screen.addshape('rpunch.gif')
		self.screen.addshape('kick.gif')
		self.screen.addshape('rkick.gif')
		self.screen.addshape('dodge.gif')
		self.screen.addshape('steady2.gif')
		self.screen.addshape('punch2.gif')
		self.screen.addshape('kick2.gif')
		self.screen.addshape('rpunch2.gif')
		self.screen.addshape('rkick2.gif')
		self.screen.addshape('dodge2.gif')
		self.don=turtle.Turtle()
		self.p2=turtle.Turtle()
		self.don.shape('steady.gif')
		self.p2.shape('steady2.gif')
		self.don.penup()
		self.p2.penup()
		self.don.goto(self.xcor,0)
		self.p2.goto(self.xcor2,0)
		self.screen.onkeypress(self.back,'a')
		self.screen.onkeypress(self.front,'s')
		self.screen.onkeypress(self.rkick,'d')
		self.screen.onkeyrelease(self.rkickRelease,'d')
		self.screen.onkeyrelease(self.stop,'a')
		self.screen.onkeyrelease(self.stop,'s')
		self.screen.onkey(self.punch,'j')
		self.screen.onkey(self.kick,'k')
		self.screen.onkey(self.dodge,'l')
		self.screen.listen()
	def update_points(self):
		if self.shape=='kick' and self.shape2=='steady' and self.xcor+163.6>=self.xcor2 and self.xcor+80<self.xcor2:
			self.points_1+=2
		elif self.shape=='punch' and self.shape2=='steady' and self.xcor+149.4>=self.xcor2 and self.xcor<self.xcor2:
			self.points_1+=1
		elif self.shape2=='kick' and self.shape=='steady' and self.xcor+163.6>=self.xcor2 and self.xcor+80<self.xcor2:
			self.points_2+=2
		elif self.shape2=='punch' and self.shape=='steady' and self.xcor+149.4>=self.xcor2 and self.xcor<self.xcor2:
			self.points_2+=1
		elif self.shape=='kick' and (self.shape2=='dodge' or self.shape2=='rkick') and self.xcor+128.2>=self.xcor2 and self.xcor+80<self.xcor2:
			self.points_1+=2
		elif self.shape=='punch' and (self.shape2=='dodge' or self.shape2=='rkick') and self.xcor+100.6>=self.xcor2 and self.xcor<self.xcor2:
			self.points_1+=1
		elif self.shape2=='kick' and (self.shape=='dodge' or self.shape=='rkick') and self.xcor+128.2>=self.xcor2 and self.xcor+80<self.xcor2:
			self.points_2+=2
		elif self.shape2=='punch' and (self.shape=='dodge' or self.shape=='rkick') and self.xcor+100.6>=self.xcor2 and self.xcor<self.xcor2:
			self.points_2+=1
		elif self.shape=='kick' and (self.shape2=='punch' or self.shape2=='rpunch') and self.xcor+163.6>=self.xcor2 and self.xcor+80<self.xcor2:
			self.points_1+=1
		elif self.shape2=='kick' and (self.shape=='punch' or self.shape=='rpunch') and self.xcor+163.6>=self.xcor2 and self.xcor+80<self.xcor2:
			self.points_2+=1
		elif self.shape=='punch' and self.shape2=='kick' and self.xcor+80>=self.xcor2 and self.xcor<self.xcor2:
			self.points_1+=1
		elif self.shape2=='punch' and self.shape=='kick' and self.xcor+80>=self.xcor2 and self.xcor<self.xcor2:
			self.points_2+=1
	def front(self):
		self.movedirection=1
	def back(self):
		self.movedirection=-1
	def stop(self):
		self.movedirection=0
	def rkick(self):
		self.movedirection=0
		if self.shape!='rkick':
			if self.rkickhold==0:
				self.rkickhold=24
				self.pshape=self.shape
				self.shape='rkick'
	def rkickRelease(self):
		if self.rkickhold<=15 and self.rkickhold>0:
			return
		self.rkickhold=0
		self.pshape=self.shape
		self.shape= 'steady'
	def punch(self):
		if self.power<=0:
			return
		if self.rkickhold<=15 and self.rkickhold>0:
			return
		self.rkickhold=0
		self.power-=1
		self.punchduration=7
		self.kickduration=0
		self.dodgeduration=0
		self.pshape=self.shape
		self.shape='punch'
	def kick(self):
		if self.power<=0:
			return
		if self.rkickhold<=15 and self.rkickhold>0:
			return
		elif self.rkickhold>=21:
			self.kickduration=self.rkickhold-16
			self.pshape='steady'
			self.shape='kick'
			self.punchduration=0
			self.dodgeduration=0
			self.rkickhold=0
			self.power-=2
			return
		else:
			self.rkickhold=0
		self.kickduration=8
		self.punchduration=0
		self.dodgeduration=0
		self.pshape=self.shape
		self.shape='kick'
		self.power-=2
	def dodge(self):
		if self.rkickhold<=15 and self.rkickhold>0:
			return
		self.rkickhold=0
		self.dodgeduration=5
		self.punchduration=0
		self.kickduration=0
		self.pshape=self.shape
		self.shape='dodge'

	def update_don(self):
		if not ((self.xcor<=-225 and self.movedirection==-1) or (self.xcor>=225 and self.movedirection==1)):
			self.xcor+=2*self.movedirection
			self.don.setx(self.xcor)
		
		if self.rkickhold:
			if self.rkickhold<=24 and self.rkickhold>=16:
				self.don.shape('rkick.gif')
				# pass
			else:
				self.shape='steady'
				self.don.shape('steady.gif')
			self.rkickhold-=1
		elif self.dodgeduration:
			self.don.shape('dodge.gif')
			self.dodgeduration-=1
		elif self.kickduration>5 and self.pshape=='rkick':
			self.don.shape('kick.gif')
			if self.kickduration==8:
				self.update_points()
			self.kickduration-=1 
		elif self.kickduration<=8 and self.kickduration>=4:
			self.don.shape('rkick.gif')
			self.shape='rkick'
			self.kickduration-=1
		elif self.kickduration and self.pshape!='rkick':
			self.don.shape('kick.gif')
			self.shape='kick'
			if self.kickduration==3:
				self.update_points()
			self.kickduration-=1
		elif self.punchduration<=7 and self.punchduration>=4:
			self.don.shape('rpunch.gif')
			self.shape='rpunch'
			self.punchduration-=1
		elif self.punchduration:
			self.don.shape('punch.gif')
			self.shape='punch'
			if self.punchduration==3:
				self.update_points()
			self.punchduration-=1
		else:
			self.don.shape('steady.gif')
			self.pshape=self.shape
			self.shape='steady'




	def front2(self):
		self.movedirection2=1
	def back2(self):
		self.movedirection2=-1
	def stop2(self):
		self.movedirection2=0
	def rkick2(self):
		self.movedirection2=0
		if self.shape2!='rkick':
			if self.rkickhold2==0:
				self.rkickhold2=24
				self.pshape2=self.shape2
				self.shape2='rkick'
	def rkickRelease2(self):
		if self.rkickhold2<=15 and self.rkickhold2>0:
			return
		self.rkickhold2=0
		self.pshape2=self.shape2
		self.shape2= 'steady'
	def punch2(self):
		if self.power2<=0:
			return
		if self.rkickhold2<=15 and self.rkickhold2>0:
			return
		self.rkickhold2=0
		self.punchduration2=7
		self.kickduration2=0
		self.dodgeduration2=0
		self.pshape2=self.shape2
		self.shape2='punch'
		self.power2-=1
	def kick2(self):
		if self.power2<=0:
			return
		if self.rkickhold2<=15 and self.rkickhold2>0:
			return
		elif self.rkickhold2>=21:
			self.kickduration2=self.rkickhold2-16
			self.pshape2='steady'
			self.shape2='kick'
			self.punchduration2=0
			self.dodgeduration2=0
			self.rkickhold2=0
			self.power2-=2
			return
		else:
			self.rkickhold2=0
		self.kickduration2=8
		self.punchduration2=0
		self.dodgeduration2=0
		self.pshape2=self.shape2
		self.shape2='kick'
		self.power2-=2
	def dodge2(self):
		if self.rkickhold2<=15 and self.rkickhold2>0:
			return
		self.rkickhold2=0
		self.dodgeduration2=5
		self.punchduration2=0
		self.kickduration2=0
		self.pshape2=self.shape2
		self.shape2='dodge'

	def update_p2(self):
		if not ((self.xcor2>=225 and self.movedirection2==1) or (self.xcor2<=-225 and self.movedirection2==-1)):
			self.xcor2+=2*self.movedirection2
			self.p2.setx(self.xcor2)
		
		if self.rkickhold2:
			if self.rkickhold2<=24 and self.rkickhold2>=16:
				self.p2.shape('rkick2.gif')
				# pass
			else:
				self.shape2='steady'
				self.p2.shape('steady2.gif')
			self.rkickhold2-=1
		elif self.dodgeduration2:
			self.p2.shape('dodge2.gif')
			self.dodgeduration2-=1
		elif self.kickduration2>5 and self.pshape2=='rkick':
			self.p2.shape('kick2.gif')
			if self.kickduration2==8:
				self.update_points()
			self.kickduration2-=1 
		elif self.kickduration2<=8 and self.kickduration2>=4:
			self.p2.shape('rkick2.gif')
			self.shape2='rkick'
			self.kickduration2-=1
		elif self.kickduration2 and self.pshape2!='rkick':
			self.p2.shape('kick2.gif')
			self.shape2='kick'
			if self.kickduration2==3:
				self.update_points()
			self.kickduration2-=1
		elif self.punchduration2<=7 and self.punchduration2>=4:
			self.shape2='rpunch'
			self.p2.shape('rpunch2.gif')
			self.punchduration2-=1
		elif self.punchduration2:
			self.shape2='punch'
			self.p2.shape('punch2.gif')
			if self.punchduration2==3:
				self.update_points()
			self.punchduration2-=1
		else:
			self.p2.shape('steady2.gif')
			self.pshape2=self.shape2
			self.shape2='steady'

	def check_points(self):
		if self.points_1>0 or self.points_2>0:
			return 1
		return 0
	# import random
	
	def chose_actions2(self):		
		cAction=realAgent([self.xcor/125,self.shape,self.xcor2/125,self.shape2,(self.power)/20,(self.power2)/20])
		if cAction==0:
			self.movedirection2=-1
		elif cAction==1:
			self.movedirection2=0
		elif cAction==2:
			self.movedirection2=1
		elif cAction==3:
			self.movedirection2=-1
			self.dodge2()
		elif cAction==4:
			self.movedirection2=0
			self.dodge2()
		elif cAction==5:
			self.movedirection2=1
			self.dodge2()
		elif cAction==6:
			self.movedirection2=-1
			self.punch2()
		elif cAction==7:
			self.movedirection2=0
			self.punch2()
		elif cAction==8:
			self.movedirection2=1
			self.punch2()
		elif cAction==9:
			self.movedirection2=0
			self.rkick2()
		elif cAction==10:
			self.movedirection2=-1
			self.kick2()
		elif cAction==11:
			self.movedirection2=0
			self.kick2()
		elif cAction==12:
			self.movedirection2=1
			self.kick2()
		elif cAction==13:
			if self.shape2=='rkick':
				self.movedirection2=-1
				self.rkickRelease2()
		elif cAction==14:
			if self.shape2=='rkick':
				self.movedirection2=-1
				self.rkickRelease2()
		elif cAction==15:
			if self.shape2=='rkick':
				self.movedirection2=-1
				self.rkickRelease2()

	def run(self):
		self.shape='steady'
		self.shape2='steady'
		self.power=20
		self.power2=20
		self.xcor=125
		self.xcor2=-125
		# self.xcor=np.random.choice(range(-224,-80))
		# self.xcor2=np.random.choice(range(80,224))
		t_end = time.time() + 20
		while time.time() < t_end:
			t2_end=time.time()+0.1
			if self.power<20:
				self.power+=0.1
			if self.power2<20:
				self.power2+=0.1
			self.chose_actions2()
			ch=random.choice([0,1])
			if ch==0:
				self.update_p2()
				self.update_don()
			else:
				self.update_don()
				self.update_p2()
			self.screen.update()
			if self.check_points():
				print(self.points_1-self.points_2)
				break
			while time.time()<t2_end:
				pass
env=Environment()
env.run()