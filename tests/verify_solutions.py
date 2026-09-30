from pathlib import Path
from collections import deque
import json, random, math, itertools, heapq, copy
ROOT=Path(__file__).resolve().parents[1]
class ListNode:
 def __init__(self,val=0,next=None): self.val,self.next=val,next
class TreeNode:
 def __init__(self,val=0,left=None,right=None):self.val,self.left,self.right=val,left,right
class Node:
 def __init__(self,val=0,next=None,random=None): self.val,self.next,self.random=val,next,random
mods={}
for p in ROOT.glob('*.py'):
 env=dict(ListNode=ListNode,TreeNode=TreeNode,Node=Node)
 exec(compile(p.read_text(),str(p),'exec'),env); mods[int(p.name.split('_')[0])]=env
covered=set(); checks=0
def call(i,*args):
 covered.add(i); obj=mods[i]['Solution'](); method=next(k for k in vars(type(obj)) if not k.startswith('_')); return getattr(obj,method)(*args)
def eq(i,args,expected):
 global checks
 result=call(i,*args); assert result==expected,(i,result,expected); checks+=1
def ll(xs):
 h=None
 for x in reversed(xs):h=ListNode(x,h)
 return h
def vals(h):
 out=[]
 while h:
  out.append(h.val);h=h.next
  assert len(out)<10000
 return out
def tree(xs):
 if not xs or xs[0] is None:return None
 root=TreeNode(xs[0]); q=deque([root]); it=iter(xs[1:])
 for n in qcopy(q,it):pass
 return root
def qcopy(q,it):
 while q:
  n=q.popleft()
  for side in ('left','right'):
   try:x=next(it)
   except StopIteration:return
   if x is not None:
    child=TreeNode(x);setattr(n,side,child);q.append(child)
  yield n
def tv(root):
 if not root:return []
 q=deque([root]);out=[]
 while q:
  n=q.popleft();out.append(n.val if n else None)
  if n:q.extend((n.left,n.right))
 while out and out[-1] is None:out.pop()
 return out
cases={
1:[(([2,7,11,15],9),[0,1]),(([3,3],6),[0,1])],
3:[(('abcabcbb',),3),(('',),0)],5:[(('cbbd',),'bb')],9:[((121,),True),((-121,),False)],11:[(([1,8,6,2,5,4,8,3,7],),49)],13:[(('MCMXCIV',),1994)],14:[((['flower','flow','flight'],),'fl')],15:[(([-1,0,1,2,-1,-4],),[[-1,-1,2],[-1,0,1]])],17:[(('23',),['ad','ae','af','bd','be','bf','cd','ce','cf'])],20:[(('([])',),True),(('(]',),False)],28:[(('sadbutsad','sad'),0),(('aaaab','aab'),2)],33:[(([4,5,6,7,0,1,2],0),4)],34:[(([5,7,7,8,8,10],8),[3,4])],35:[(([1,3,5,6],2),1)],42:[(([0,1,0,2,1,0,1,3,2,1,2,1],),6)],43:[(('123','456'),'56088')],50:[((2.0,-2),.25)],53:[(([-2,1,-3,4,-1,2,1,-5,4],),6)],58:[((' hello world  ',),5)],66:[(([9,9],),[1,0,0])],67:[(('1010','1011'),'10101')],69:[((8,),2)],96:[((3,),5)],121:[(([7,1,5,3,6,4],),5)],125:[(('A man, a plan, a canal: Panama',),True)],136:[(([4,1,2,1,2],),4)],152:[(([2,3,-2,4],),6)],167:[(([2,7,11,15],9),[1,2])],169:[(([2,2,1,1,1,2,2],),2)],200:[(([list('110'),list('010'),list('001')],),2)],209:[((7,[2,3,1,2,4,3]),2)],217:[(([1,2,1],),True)],219:[(([1,2,3,1],3),True)],231:[((16,),True),((0,),False)],268:[(([3,0,1],),2)],438:[(('cbaebabacd','abc'),[0,6])],485:[(([1,1,0,1,1,1],),3)],496:[(([4,1,2],[1,3,4,2]),[-1,3,-1])],498:[(([[1,2,3],[4,5,6],[7,8,9]],),[1,2,4,7,5,3,6,8,9])],503:[(([1,2,1],),[2,-1,2])],560:[(([1,1,1],2),2)],567:[(('ab','eidbaooo'),True)],594:[(([1,3,2,2,5,2,3,7],),5)],643:[(([1,12,-5,-6,50,3],4),12.75)],680:[(('abca',),True)],704:[(([-1,0,3,5,9,12],9),4)],713:[(([10,5,2,6],100),8)],724:[(([1,7,3,6,5,6],),3)],733:[(([[1,1,1],[1,1,0],[1,0,1]],1,1,2),[[2,2,2],[2,2,0],[2,0,1]])],739:[(([73,74,75,71,69,72,76,73],),[1,1,4,2,1,1,0,0])],744:[((['c','f','j'],'c'),'f')],868:[((22,),2)],904:[(([1,2,3,2,2],),4)],939:[(([[1,1],[1,3],[3,1],[3,3],[2,2]],),4)],994:[(([[2,1,1],[1,1,0],[0,1,1]],),4)],1004:[(([1,1,1,0,0,0,1,1,1,1,0],2),6)],1009:[((5,),2),((0,),1)],1200:[(([4,2,1,3],),[[1,2],[2,3],[3,4]])],1323:[((9669,),9969)],1356:[(([0,1,2,3,4,5,6,7,8],),[0,1,2,4,8,3,5,6,7])],1404:[(('1101',),6)],1464:[(([3,4,5,2],),12)],1470:[(([2,5,1,3,4,7],3),[2,3,5,4,1,7])],1784:[(('1001',),False)],1877:[(([3,5,2,3],),7)],1922:[((4,),400)],1929:[(([1,2,1],),[1,2,1,1,2,1])],1984:[(([9,4,1,7],2),2)],2197:[(([6,4,3,2,7,6,2],),[12,7,6])],2348:[(([1,3,0,0,2,0,0,4],),6)],2461:[(([1,5,4,2,9,9,9],3),15)],2540:[(([1,2,3],[2,4]),2)],2553:[(([13,25,83,77],),[1,3,2,5,8,3,7,7])],2976:[(('abcd','acbe',['a','b','c','c','e','d'],['b','c','b','e','b','e'],[2,5,5,1,2,20]),28)],2977:[(('abcdefgh','acdeeghh',['bcd','fgh','thh'],['cde','thh','ghh'],[1,3,5]),9),(('abcd','abce',[],[],[]),-1)],3000:[(([[9,3],[8,6]],),48)],3612:[(('a#b%*',),'ba')],3650:[((4,[[0,1,3],[3,1,1],[2,3,4],[0,2,2]]),5)],3651:[(([[1,3,3],[2,5,4],[4,3,5]],2),7),(([[1,2],[2,3],[3,4]],1),9)],3823:[((')ebc#da@f(',),'(fad@cb#e)')],3824:[(([3,7,5],),3)],3827:[((4,),3)],3912:[(([1,2,4,2,3,2],),[1,2,4,3,2])]
}
for i,items in cases.items():
 for args,want in items:eq(i,args,want)
for i,x,args,want in [(19,[1,2,3,4,5],(2,),[1,2,3,5]),(24,[1,2,3,4],(),[2,1,4,3]),(61,[1,2,3,4,5],(2,),[4,5,1,2,3]),(83,[1,1,2,3,3],(),[1,2,3]),(92,[1,2,3,4,5],(2,4),[1,4,3,2,5]),(148,[4,2,1,3],(),[1,2,3,4]),(206,[1,2,3],(),[3,2,1]),(328,[1,2,3,4,5],(),[1,3,5,2,4]),(876,[1,2,3,4],(),[3,4]),(2095,[1,3,4,7,1,2,6],(),[1,3,4,1,2,6])]:
 assert vals(call(i,ll(x),*args))==want,i;checks+=1
assert vals(call(2,ll([2,4,3]),ll([5,6,4])))==[7,0,8];checks+=1
assert vals(call(21,ll([1,2,4]),ll([1,3,4])))==[1,1,2,3,4,4];checks+=1
for i,x,arg,want in [(26,[1,1,2],(),[1,2]),(27,[3,2,2,3],(3,),[2,2])]:
 k=call(i,x,*arg); assert x[:k]==want;checks+=1
for i,x,arg,want in [(75,[2,0,2,1,1,0],(),[0,0,1,1,2,2]),(189,[1,2,3,4,5,6,7],(3,),[5,6,7,1,2,3,4]),(283,[0,1,0,3,12],(),[1,3,12,0,0])]:
 call(i,x,*arg); assert x==want,(i,x,want);checks+=1
x=[1,2,3,0,0,0];call(88,x,3,[2,5,6],3);assert x==[1,2,2,3,5,6];checks+=1
result=call(49,['eat','tea','tan','ate','nat','bat']);assert sorted(map(sorted,result))==sorted(map(sorted,[['eat','tea','ate'],['tan','nat'],['bat']]));checks+=1
board=[list(s) for s in ['53..7....','6..195...','.98....6.','8...6...3','4..8.3..1','7...2...6','.6....28.','...419..5','....8..79']];eq(36,(board,),True)
for i,method in [(155,'MinStack'),(225,'MyStack')]:
 covered.add(i);obj=mods[i][method]();obj.push(3);obj.push(1);assert obj.top()==1
 if i==155:assert obj.getMin()==1
 obj.pop();assert obj.top()==3;checks+=1
for i,data,args,want in [(94,[1,None,2,3],(),[1,3,2]),(102,[3,9,20,None,None,15,7],(),[[3],[9,20],[15,7]]),(103,[3,9,20,None,None,15,7],(),[[3],[20,9],[15,7]]),(104,[3,9,20,None,None,15,7],(),3),(110,[1,2,2,3,3,None,None,4,4],(),False),(111,[2,None,3,None,4],(),3),(112,[1,2,3],(3,),True),(113,[5,4,8,11,None,13,4,7,2,None,None,5,1],(22,),[[5,4,11,2],[5,8,4,5]]),(124,[-10,9,20,None,None,15,7],(),42),(129,[1,2,3],(),25),(144,[1,None,2,3],(),[1,2,3]),(145,[1,None,2,3],(),[3,2,1]),(199,[1,2,3,None,5,None,4],(),[1,3,4]),(222,[1,2,3,4,5,6],(),6),(230,[3,1,4,None,2],(1,),1),(257,[1,2,3,None,5],(),['1->2->5','1->3']),(404,[3,9,20,None,None,15,7],(),24),(543,[1,2,3,4,5],(),3),(563,[1,2,3],(),1),(637,[3,9,20,None,None,15,7],(),[3.,14.5,11.]),(671,[2,2,5,None,None,5,7],(),5),(1448,[3,1,4,3,None,1,5],(),4)]:eq(i,(tree(data),)+args,want)
eq(100,(tree([1,2,3]),tree([1,2,3])),True);eq(101,(tree([1,2,2,3,4,4,3]),),True)
eq(572,(tree([3,4,5,1,2]),tree([4,1,2])),True)
assert tv(call(226,tree([4,2,7,1,3,6,9])))==[4,7,2,9,6,3,1];checks+=1
assert tv(call(700,tree([4,2,7,1,3]),2))==[2,1,3];checks+=1
assert tv(call(701,tree([4,2,7,1,3]),5))==[4,2,7,1,3,5];checks+=1
for i in (235,236):
 root=tree([6,2,8,0,4,7,9,None,None,3,5]);assert call(i,root,root.left,root.left.right) is root.left;checks+=1
for i in (141,142):
 head=ll([3,2,0,-4]);entry=head.next;head.next.next.next.next=entry
 result=call(i,head);assert result is (True if i==141 else entry);checks+=1
common=ll([8,4,5]);a=ListNode(1,common);b=ListNode(2,ListNode(3,common));assert call(160,a,b) is common;checks+=1
h=ll([1,2,2,1]);eq(234,(h,),True);assert vals(h)==[1,2,2,1]
a,b=Node(7),Node(13);a.next=b;b.random=a;clone=call(138,a);assert clone is not a and clone.next.random is clone and clone.next.val==13;checks+=1
for n in range(1,10):
 x=call(1304,n);assert len(x)==len(set(x))==n and sum(x)==0;checks+=1
# Randomized comparisons with independent exhaustive references.
rng=random.Random(20260930)
for _ in range(120):
 nums=[rng.randint(-4,5) for _ in range(rng.randint(1,9))];n=len(nums);k=rng.randint(-3,5)
 eq(560,(nums,k),sum(sum(nums[i:j])==k for i in range(n) for j in range(i+1,n+1)))
 eq(53,(nums,),max(sum(nums[i:j]) for i in range(n) for j in range(i+1,n+1)))
 eq(152,(nums,),max(math.prod(nums[i:j]) for i in range(n) for j in range(i+1,n+1)))
 positive=[abs(x)+1 for x in nums];limit=rng.randint(0,30)
 eq(713,(positive,limit),sum(math.prod(positive[i:j])<limit for i in range(n) for j in range(i+1,n+1)))
 eq(3824,(positive,),next(t for t in range(1,100) if sum((x+t-1)//t for x in positive)<=t*t))
 eq(3912,(nums,),[x for i,x in enumerate(nums) if all(x>y for y in nums[:i]) or all(x>y for y in nums[i+1:])])
 heights=[abs(x) for x in nums]
 eq(42,(heights,),sum(max(0,min(max(heights[:i+1]),max(heights[i:]))-x) for i,x in enumerate(heights)))
 m=n=3;g=[[rng.randrange(6) for _ in range(n)] for _ in range(m)];k=rng.randrange(3)
 # Full state graph is slower but independent of the optimized teleport DP.
 d={(0,0,0):0};heap=[(0,0,0,0)]
 while heap:
  cost,r,c,t=heapq.heappop(heap)
  if cost!=d[(r,c,t)]:continue
  moves=[(a,b,t,g[a][b]) for a,b in ((r+1,c),(r,c+1)) if a<m and b<n]
  if t<k:moves += [(a,b,t+1,0) for a in range(m) for b in range(n) if g[a][b]<=g[r][c]]
  for a,b,nt,w in moves:
   state=(a,b,nt);nc=cost+w
   if nc<d.get(state,math.inf):d[state]=nc;heapq.heappush(heap,(nc,a,b,nt))
 eq(3651,(g,k),min(d.get((m-1,n-1,t),math.inf) for t in range(k+1)))
# Boundary cases for new and difficult problems.
for n in range(1001):eq(3827,(n,),sum(len(set(bin(x)[2:]))==1 for x in range(n+1)))
eq(2977,('aaaa','bbbb',['a','aa','c'],['c','bb','b'],[2,3,2]),6)
eq(2977,('abcd','abcd',[],[],[]),0)
eq(3650,(3,[[0,1,1]]),-1)
eq(3651,([[0,0],[0,0]],0),0)
# Deep skewed trees exercise iterative traversals beyond Python's recursion limit.
deep=TreeNode(1);node=deep
for _ in range(1999):node.right=TreeNode(1);node=node.right
eq(104,(deep,),2000);eq(543,(deep,),1999);eq(110,(deep,),False)
missing=set(mods)-covered
assert not missing,missing
print(json.dumps({'solution_files':len(mods),'files_exercised':len(covered),'checks_passed':checks,'random_seed':20260930}))
