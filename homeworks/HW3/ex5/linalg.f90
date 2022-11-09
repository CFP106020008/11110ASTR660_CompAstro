module linalg

    ! ---------------------------------------------------------
    ! ref: https://rosettacode.org/wiki/LU_decomposition#Fortran
    ! ---------------------------------------------------------

    implicit none
    contains 


        subroutine mat_print(amsg,a)
            character(*), intent(in) :: amsg
            class    (*), intent(in) :: a(:,:)
            integer                  :: i
            print*,' '
            print*,amsg
            do i=1,size(a,1)
                select type (a)
                    type is (real(8)) ; print'(100f8.3)',a(i,:)
                    type is (integer) ; print'(100i8  )',a(i,:)
                end select
            end do
            print*,' '
        end subroutine

        subroutine solve_lower_triangular_matrix(N,L,b,x)
            implicit none

            integer, intent(in)  :: N
            real, dimension(N,N), intent(in)  :: L  ! lower triangle
            real, dimension(N)  , intent(in)  :: b  ! vector
            real, dimension(N)  , intent(out) :: x  ! solution
            real, dimension(N)  :: bs              

            integer :: i,j
        
            bs = b 
            do j = 1,N 
                if (L(j,j) .EQ. 0.0) then
                        stop
                endif

                x(j) = bs(j)/L(j,j)
                do i = j+1,N 
                        bs(i) = bs(i)-L(i,j)*x(j)
                enddo

            enddo

            return
        end subroutine solve_lower_triangular_matrix

        subroutine solve_upper_triangular_matrix(N,U,b,x)
            implicit none

            integer, intent(in)  :: N
            real, dimension(N,N), intent(in)  :: U  ! upper triangle
            real, dimension(N)  , intent(in)  :: b  ! vector
            real, dimension(N)  , intent(out) :: x  ! solution
            real, dimension(N)  :: bs

            integer :: i,j

            bs = b
            do j=N,1,-1
                if (U(j,j) .EQ. 0.) then
                        stop
                endif
                x(j) = bs(j)/U(j,j)
                do i = 1,N-1
                        bs(i) = bs(i)-U(i,j)*x(j)
                enddo
            enddo

            return
        end subroutine solve_upper_triangular_matrix

        subroutine LU_decomposition(N,A,L,U)
            implicit none
            
            integer, intent(in)  :: N
            real, dimension(N,N), intent(in)  :: A    ! matrix
            real, dimension(N,N), intent(out)    :: L,U  ! matrix
            real, dimension(N,N) :: M, As
 
            integer :: i,j,k

            As = A
            M = 0.0
            U = 0.0
            do k = 1,N-1
                if (A(k,k) .eq. 0.) then
                   stop
                endif
                
                do i = k+1,N
                   M(i,k) = As(i,k)/As(k,k)
                enddo

                do j = k+1,N
                   do i = k+1,N
                      As(i,j) = As(i,j)-M(i,k)*As(k,j)
                   enddo
                enddo
            enddo            

            L = M
            !diagonal of L equals 1
            do i = 1,N
                L(i,i) = 1.0
            enddo
            
            ! U are the upper triangular part of As    
            do j = 1,N
                do i = 1,N
                   if (j >= i) then
                      U(i,j)=As(i,j)
                   endif
                enddo
            enddo

        end subroutine LU_decomposition

        subroutine solve_lu(N,A,b,x)
            ! solve: A x = b (LUx = b, Ly=b, y=Ux)
            integer, intent(in)  :: N
            real, dimension(N,N), intent(in)  :: A  ! upper triangle
            real, dimension(N)  , intent(in)  :: b  ! vector
            real, dimension(N)  , intent(out) :: x  ! solution

            real, dimension(N,N) :: L, U, P
            real, dimension(N)   :: y, pb

            call LU_decomposition(N,A,L,U)
            call solve_lower_triangular_matrix(N,L,b,y) ! Ly = b
            call solve_upper_triangular_matrix(N,U,y,x) ! Ux = y

        end subroutine solve_lu

end module linalg
