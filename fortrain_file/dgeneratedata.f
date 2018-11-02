      SUBROUTINE GENERATEDATA(NT)

		  IMPLICIT NONE

      INTEGER NT
      integer i,j,k
      character filename*5

      real*8 file_num
      common /generate/file_num

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

      IF(MOD(NT+1,3).EQ.0)THEN
      write(filename,'(i5.5)') int(file_num)
      file_num=file_num+1
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

      print *,'The NT is ',NT,' 777'
      print *,file_num,' has been done.'
      ENDIF

      END
    