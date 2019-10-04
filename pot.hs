pot n m = if(m==0)
 then 1
 else if(m==1)
  then n
  else (pot n (m-1)) * n