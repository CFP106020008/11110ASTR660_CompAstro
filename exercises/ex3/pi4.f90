program pi

  implicit none
  
  integer :: i
  real :: area,rela_err
  integer :: N

  character(len=20) :: file_name
  character(len=20) :: formated

  real, parameter :: real_PI = 4.0*atan(1.0)
  integer, parameter :: NMAX = 7
  integer, dimension(NMAX) :: n_iteration

  n_iteration = (/10,100,1000,10000,&
                  100000,1000000,10000000/)

  file_name = "pi_error.dat"
  formated = "(I8,E9.3E1)"

  open(unit=3, file=file_name)
 
  do i = 1,NMAX
        area = 0.
        N = n_iteration(i)
        call compute_integral(N,area)  
  
        print *, "Area=",area 
        print *, " PI =",(2.*area)   
        rela_err = (real_PI-2*area)/real_PI
        write(3,formated) N,rela_err
  enddo
  close(3)

end program

subroutine compute_integral(N,A) 

  implicit none
  integer, intent(IN) :: N
  real, intent(OUT) :: A
   
  real :: dx
  real :: x,h,dA
  integer :: i
  real :: my_func

  dx = 2./real(N)
  do i = 1,N-1
     x = dx/2.+dx*(i-N/2)
     h = my_func(x)
     dA = dx*h
     A = A+dA
  enddo

  return

end subroutine compute_integral

real function my_func(x)
  real :: x
  my_func = sqrt(1.-x**2.)
  return
end function
