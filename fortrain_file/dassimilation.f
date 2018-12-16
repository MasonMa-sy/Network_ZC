      SUBROUTINE assimilation(NT,IT1)

      implicit none

      INTEGER NT,IT1
      integer i,j,k,l
      character filename*5
      real*8 file_num,windstress(34,30,2),wind_file_num,afa(30)
      real*8 start_num

      common /generate/file_num,start_num

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

cc--------add the function at this area.
cc compute the wind stress anomalies.....................................
c      CALL STRESS(TD,ISTART)
c
cc insert the stress forcing in ocean model..............................
c      CALL CFORCE
c
cc for wind stress data assimilation....................add by mashaoyang
c      CALL assimilation(NT,IT1)
c
c400   CONTINUE
      
      wind_file_num = IT1 - 48 - 120 - 1
      IF(wind_file_num.GT.start_num) GO TO 900  

c      IF(MOD(NT,3).EQ.1)THEN
c      print *,'The wind_file_num ',wind_file_num,' 666 ',IT1
      
      afa(:)=0.55d0
      do i=13,15
        afa(i)=afa(i)-0.1d0*(i-12)
      enddo
      do i=16,18
        afa(i)=afa(i)-0.1d0*(19-i)
      enddo

      write(filename,'(i5.5)') int(wind_file_num)
      open(unit=375,
     & file='data_wind/data_wind_'//filename//'.dat',
     & form='binary',status='old', action='read')
      do l=1,2
      do i=1,30
      do j=1,34
        read( 375 ) windstress(j,i,l)
      enddo
      enddo
      enddo
      Close( 375 )

      do l=1,2
c      do i=6,25
c      do j=6,32
      do i=6,26
      do j=6,32
        HTAU(j,i,l)=afa(i)*windstress(j,i,l)+(1-afa(i))*HTAU(j,i,l)
      enddo
      enddo
      enddo

c      ENDIF

900   CONTINUE

      END
