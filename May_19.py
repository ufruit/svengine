#!user/bin/env python

import tempfile,os,string

generation=3 #add a warning not let genaration bigger than real generation

#tree1=open('/home/lichao/Documents/github/svengine/tree1','w+b')
#for G,line in enumerate(o):
#	print G,line
#home=tempfile.TempFile()
#print 

class Node:
	def __init__(self,i,j,v,a):#i:int,j:int,v:dict,a:range[0,1]
		self.i=int(i)
		self.j=int(j)
		self.v=v
		self.a=float(a)

#treefile=file('/home/lichao/Documents/github/svengine/exam_tree')
#def trefil2varfile()

def P(Node):	#find Node's parent
	i=Node.i-1
	j=Node.j/2
	return locals()['N'+str(i)+str(j)]

def C(Node):	#find Node's children
	i=Node.i+1
	j1=Node.j+1
	j2=Node.j+2	
	return [locals()['N'+str(i)+str(j1)],locals()['N'+str(i)+str(j2)]]

def get_name(Node):
	d=locals()
	for key in d:
		if d[key]==Node:
			return key
	
Nodelist=[]
with open('/home/lichao/Documents/github/svengine/exam_tree') as treefile:
#	treefile=file

#	with open('/home/lichao/Documents/github/svengine/tree1','w+') as tree1:
#tree1=open('/home/lichao/Documents/github/svengine/tree1','w+')
#tree1=tempfile.TemporaryFile()
#tree1=open('tree1','w+')
		for g,line in enumerate(treefile):
			if '/' not in line and g<=2*generation:
				#tree1.write(line)
				line=line.expandtabs().strip().split(' ')
				while '' in line:
					line.remove('')		
				l=len(line)
				
				if g==0:# the root node
					print line	
					assert  line==['N'],	"the tree should use N as root Node"
					locals()['N'+'0'+'0']=Node(0,0,{'Normal':None},1)
					Nodelist.append(N00)
				else:
					for j in range(l) :		
						
						if line[j]=='None':	#check the 'None' condition
							#print line[j],type(line[j])							
							locals()['N'+str(g/2)+str(j)]=Node(g/2,j,locals()['N'+str(g/2-1)+str(int(j/2))].v,0.5)
							Nodelist.append(get_name(Node(g/2,j,locals()['N'+str(g/2-1)+str(int(j/2))].v,0.5)))
						else:
						
							
						
							

							line[j]=line[j].split(';')
							
							var=line[j][0].split(',')
							print var#,N00,N00.i,N00.j,N00.v,N00.a
							freq=line[j][1]					
						
							#print var.split(':')[0],var.split(':')[1],var,type(var)
						
							if var[0][0]=='N' and var[0][1].isdigit() :
								assert len(var)==1,	"Normal Node only have one type 'N'"	
								locals()['N'+str(g/2)+str(j)]=Node(g/2,j,{'Normal':None},freq)	
								Nodelist.append(get_name(Node(g/2,j,{'Normal':None},freq)))
							else:
		
	#						line[j]=line[j].split(';')
	#						b=line[j][0]
								varlist={}
							#freq=line[j][1]
							#print varlist
								map(lambda x:varlist.setdefault(x.split(':')[0], int(x.split(':')[1])), var)
								locals()['N'+str(g/2)+str(j)]=Node(g/2,j,varlist,freq)
								Nodelist.append(get_name(Node(g/2,j,varlist,freq)))
					#if line[j].startwith('N'):
					#	locals()['N'+g/2+j]=Node(g/2,j,varlist,freq)
print Nodelist,	'this the all Node!'
assert len(Nodelist)==2**(generation+1)-1,	'the number of Node should equal to 2**(generation+1)-1, the treefile may include error.'	
#for i in range(15):
#	print Nodelist[i].i,Nodelist[i].j,Nodelist[i].v,Nodelist[i].a	
#print N32.v,N21.v,N32.a		
print get_name(Node(0,0,{'Normal':None},1))
print locals()['N00']	==	Node(0,0,{'Normal':None},1)
print locals()
#Nodelist1=[]
#print N11.i,N11.j,N11.v,N11.a				
#for g in range(generation+1):
#	for j in range(2**g):
#		Nodelist1.append(locals()['N'+str(g)+str(j)])
#print [N00,N10,N11]
#print ''
#for line in tree1:
#				print g/2,line  #g/2 because '/' was remove
#quit()
#		with open('/home/lichao/Documents/github/svengine/tree2','w+') as tree2:
#			for g,line in enumerate(tree1):
#				print g,line
#				if g<=generation :
#					tree2.write(line)
#
#	quit()
	#tree2=open('/home/lichao/Documents/github/svengine/tree2')


#A00=Node(0,0,{'var1':1},0.5)
#print A00,A00.i,A00.j,A00.v,A00.a,type(A00.v)	
			#for g,line in enumerate(tree2):
	#line=line.expandtabs().strip().split(' ')
	#string.translate(line, del=" ")
	#line=line.strip().split(' ')
	#line=line.split(' ')
	
#	while '' in line:
#		line.remove('')
#	l=len(line)
#	for j in range(l):
#		line[j]=line[j].split(';')
#		varlist=line[j][0]
#		print varlist
#		a={}
	#	map(lambda x:a.setdefault(x.split(':')[0], x.split(':')[1]), varlist)
	#	if line[j].startwith('N'):
	#		locals()['N'+g+j]=	
		
	
		
	#print line	
		#if :
			
	#print line,l
#for g,line in enumerate(tree2):
#	print g,line
#for line in tree1:
#	print line	
	
#tree1.close()
