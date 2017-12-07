class mtwist:
	def __init__(self,tmpseed=0,n=624,m=397):
		
		self.n=n              #degree of recurrence
		self.state=[0]*self.n #states created
		self.m=m              #middle word offset
		self.w=32
		self.r=27
		self.b=0x9D2C5680     #bitmask
		self.c=0xEFC60000     #bitmask
		self.d=0xFFFFFFFF     #bitmask
		self.s=7              #bitshift R
		self.t=12             #bitshift R
		self.u=11             #bitshift L
		self.l=18             #bitshift L
		self.a=0x9908B0DF     #conditional xor
		self.f=938014277
		self.upper_mask=3<<30
		self.index=0
		self.state[0]=tmpseed
		if(tmpseed==0):
			import time
			self.state[0]=hash(time.clock())
		for x in range(1,624):
			self.state[x]=(self.state[x-1]^(self.state[x-1]>>30)+x ) & 0xFFFFFFFF

	def twistar(self):
		for x in range(0,624):	
			temp = (self.state[x]& self.upper_mask)+(self.state[(x+1)% self.n]&(self.uppermask ^ 0xFFFFFFFF))
			if temp%2 != 0:
				temp_shift = (temp>>1)^ self.a
			else:
				temp_shift = temp>>1
			self.state[x] = self.state[((x+self.m)%self.n)]^temp_shift
		self.index=0
                
	def randtw(self,a,b,tp='i'):
		if (self.index >= self.n):
			self.twistar()
		r1=self.state[self.index]
		r2=r1^(r1>>self.u) & self.d
		r2=r2^(r2<<self.s) & self.b
		r2=r2^(r2<<self.t) & self.c
		res=r2^(r2>>self.l)
		self.index+=1
		temp=res & 0xFFFFFFFF
		if (tp=='i'):
			return int((a+temp%(b-a)))
