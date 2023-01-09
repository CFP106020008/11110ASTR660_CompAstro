module IO
    implicit none
    contains
        subroutine output(n,time)
            use Simulation_data
            implicit none
            integer, intent(in) :: n
            real, intent(in)    :: time

            integer      :: i,j
            character(7) :: cycstr
            character(58)      :: filename

            real         :: ua ! analytical solution
            real         :: pa, pi, pe
            
            write(cycstr,10) n,'.d'
10  format(i5,a2)

            ! fill remaing zeros
            do i=1,5
                if(cycstr(i:i).eq.' ') cycstr(i:i)='0'
            enddo

            filename = 'advection_'//cycstr
            open(100,file=filename,status='unknown')

            ! write header
            write(100,29) "# i","# j", "x", "y", "U(x,y)"

            !pa = 0.15 + cx * time
            !pi = pa-0.05
            !pe = pa+0.05

            do j = 1, jend
                do i=1,iend
                    !if ( (x(i) .ge. pi) .and. (x(i) .le. pe) ) then
                    !    ua = 1.0
                    !else
                    !    ua = 0.01
                    !endif
                    write(100,30) i, j, x(i), y(j), u(i,j)
                enddo
            enddo

29 format(2a6,3a24)
30 format(2i6,3e24.12)

            close(100)
            return
        end subroutine output

end module IO
