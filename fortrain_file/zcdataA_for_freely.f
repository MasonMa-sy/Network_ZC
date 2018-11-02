      Program zcdata

      implicit none
      Integer,parameter::particleSize=20
      Integer,parameter::swarmSize=150
      Real*8,parameter::particleScope=1.0
!      Integer, Parameter::nsample=60
      Integer, Parameter::mx=30
      Integer, Parameter::my=34
      Integer, Parameter::totalDim=1080
      Real*8 center,th_part(totalDim,particleSize),delta,
     & ssta_cnop(mx,my),h1a_cnop(mx,my),ssta_end(mx,my),h1a_end(mx,my)
      Real*8 ssta(mx,my),h1a(mx,my)
      Integer loopCount
      Real timeBegin,timeEnd,timeMid


!c Declare the variables related to ZC model.

      integer i,j,k,ipertur,jpertur,i1,i2,irec,for_circle

      real*8 tinitial,tfinal, file_num, rand_temp
      real*8 normtobasis_init,normtocnop,normtocnop_tlm,normtocnop_nlm
      real*8 normh1basis_init,normh1cnop,normh1cnop_tlm,normh1cnop_nlm
      real*8 normxbasis_init,normxcnop,normxcnop_tlm,normxcnop_nlm
      character filename*5

      real*8 toinit(mx,my),toend(mx,my)
      real*8 topurb0(mx,my),topurb1(mx,my)
      real*8 totalinit(mx,my),totalend(mx,my)
      real*8 tocnop(mx,my),tocnop_tlm(mx,my),tocnop_nlm(mx,my)

      real*8 h1init(mx,my),h1end(mx,my)
      real*8 h1purb0(mx,my),h1purb1(mx,my)
      real*8 h1talinit(mx,my),h1talend(mx,my)
      real*8 h1cnop(mx,my),h1cnop_tlm(mx,my),h1cnop_nlm(mx,my)

      integer imax,jmax
      real*8 maxtopurb0,maxh1purb0
      real*8 maxtocnop,maxh1cnop
      real*8 normxpurb0
      
      common /r8/toinit,h1init,toend,h1end
      common /r9/tinitial,tfinal
      common /r10/ipertur,jpertur
      common /generate/file_num

c---for test mean sst
      REAL*8 H1(30,34),U1(30,34),V1(30,34)
      COMMON/ZDAT2/H1,U1,V1

      REAL*8 Q0O(30,34),UO(30,34),VO(30,34),DO(30,34),HTAU(34,30,2),
     B TO(30,34),US(30,34),VS(30,34),
     C WP(30,34),DT1(30,34,7),TT(30,34),UV1(30,34),UV2(30,34),
     D WM1(30,34),UAT(30,34),VAT(30,34),DIVT(30,34)

      REAL WM(30,34,2,12),DIVM(30,34,12),
     +     SSTM(30,34,12),WEM(30,34,12),UV(30,34,2,12)

      COMMON/ZDATA/WM,DIVM,Q0O,SSTM,UO,VO,DO,HTAU,WEM,TO,UV,
     A US,VS,WP,DT1,TT,UV1,UV2,WM1,UAT,VAT,DIVT
c---end


      tinitial=0.5d0
      tfinal=tinitial+12060.0d0
      call initialbasic(toinit,h1init)
c      call bfmodel(toinit,h1init,toend,h1end)
      file_num=0
      
      write(filename,'(i5.5)') int(file_num)
      open(unit=374,file='data/data_'//filename//'.dat',
     & form='binary',status='replace')
      do i=6,25
      do j=6,32
      Write(374) TO(i,j)
      enddo
      enddo
      do i=6,25
      do j=6,32
      Write(374) H1(i,j)
      enddo
      enddo
      close(374)

c      tfinal=tinitial+12.0d0
      file_num=file_num+1                
        
      call bfmodel(toinit,h1init,ssta_end,h1a_end)

      write(filename,'(i5.5)') int(file_num)
      open(unit=374,file='data/data_'//filename//'.dat',
     & form='binary',status='replace')  

      do i=6,25
      do j=6,32
      Write(374) TO(i,j)
      enddo
      enddo
      do i=6,25
      do j=6,32
      Write(374) H1(i,j)
      enddo
      enddo
      close(374)
c      print *,file_num,' has been done.'      
c      print *,'The ',for_circle,' has been done.'
c---test msst
c---integral ZC for nature.
c---end 
      
      end