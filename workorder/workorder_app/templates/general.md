# 

class JobName
   jobname 
   address
   generalcontractor 



class WorkOrder
    id (prepopulated)
    jobname (foreign key)
    workperformed

1:1 relationship between Workorder and material
1:Many relationship between Jobname and Workorder
class material
    id
    quantity
    product

carpenter - foreman carpenter - # of employees, reg hours, premium hours
carpenter - journeyman carpenter - # of employees, reg hours, premium hours
taper - # of employees, reg hours, premium hours
taper foreman - # of employees, reg hours, premium hours
laborer - # of employees, reg hours, premium hours

for signature
    Authorized By
    Title of person to sign
    signature
    signature of contractor
