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

c---for test mean sst
      REAL*8 Q0O(30,34),UO(30,34),VO(30,34),DO(30,34),HTAU(34,30,2),
     B TO(30,34),US(30,34),VS(30,34),
     C WP(30,34),DT1(30,34,7),TT(30,34),UV1(30,34),UV2(30,34),
     D WM1(30,34),UAT(30,34),VAT(30,34),DIVT(30,34)

      REAL WM(30,34,2,12),DIVM(30,34,12),
     +     SSTM(30,34,12),WEM(30,34,12),UV(30,34,2,12)

      COMMON/ZDATA/WM,DIVM,Q0O,SSTM,UO,VO,DO,HTAU,WEM,TO,UV,
     A US,VS,WP,DT1,TT,UV1,UV2,WM1,UAT,VAT,DIVT
c---end

c---for the same time and random. ssta 0.4,h1a 6

c     tinitial=40.5
c     tfinal=tinitial+9.0d0
      call initialbasic(toinit,h1init)
c      call CPU_TIME(timeBegin)
      call bfmodel(toinit,h1init,toend,h1end)
c      call CPU_TIME(timeMid)
      file_num=0

      call random_seed()

      do for_circle = 1, 3000, 1

      do i=1,30
      do j=1,34
        ssta(i,j)=0
        h1a(i,j)=0
      enddo
      enddo

200     format(34(1x,f12.5))
      
      do i=6,25
      do j=6,32
        call random_number(rand_temp)
        ssta(i,j)=-0.4 + 0.8*rand_temp
        call random_number(rand_temp)
        h1a(i,j)=-6.0 + 12.0*rand_temp
      enddo
      enddo
      write(filename,'(i5.5)') int(file_num)
      open(unit=374,file='data/data_in_'//filename//'.dat',
     & form='formatted',status='replace')
      write(374,200)(ssta(i,:),i=1,30)
      write(374,200)(h1a(i,:),i=1,30)
      close(374)

c---for the same time and random. ssta 0.3,h1a 6
	    do tinitial=48.5,48.5,1.0d0
        tfinal=tinitial+9.0d0
        
c        print *,'###',filename,'%%%',tinitial
      open(unit=374,file='data/data_out_'//filename//'.dat',
     & form='formatted',status='replace')        
c        open(unit=375,file='1toh1end.dat',
c       & form='formatted',status='replace')                   
        
        call bfmodel(ssta,h1a,ssta_end,h1a_end)

        write(374,200)(ssta_end(i,:),i=1,30)
        write(374,200)(h1a_end(i,:),i=1,30)
c        write(375,200)(toend(i,:),i=1,30)
c        write(375,200)(h1end(i,:),i=1,30)
        close(374)
c        close(375)
        print *,file_num,' has been done.'
      end do
      file_num=file_num+1
      print *,'The ',for_circle,' has been done.'
      end do
c---test msst
c      write(374,200)(TT(i,:),i=1,30)
c      tinitial=tfinal
c      tfinal=tinitial+1
c      call initialbasic(toinit,h1init)
c      call bfmodel(toinit,h1init,toend,h1end)
c      call CPU_TIME(timeEnd)
c      write(375,200)(TT(i,:),i=1,30)
c      print *,'Time ',timeEnd,'#',timeMid,'#',timeBegin,' (s)'
c---end 
      
      end