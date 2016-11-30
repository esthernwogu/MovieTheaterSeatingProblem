# MovieTheaterSeatingProblem

Problem:
    -Implement an Algorithm to assign movie theater seats to satisfy reservation requests.    
    
Assumptions:
    -10 rows x 20 seats    
                          [  SCREEN  ]
                       A  SSSSSSSSSSSS
                       B  SSSSSSSSSSSS
                       C  SSSSSSSSSSSS
                       .  SSSSSSSSSSSS
                       .  SSSSSSSSSSSS
                       J  SSSSSSSSSSSS
                          1   ...   20
Input:
    - A file consisting of 2 columns: 1st column, reservation number; 2nd column, seat requests
    - e.g.
        T001 4
        T002 6
        T003 1
        ...
Output:
    - A file in which each line contains a reservation number and the seat names assigned for that reservation
    - e.g.
        T001 A4, A5, A6, A7
        T002 G2, G3, G4, G5, G6, G7
        T003 H9
        ...   
        
My Solution:
    This problem seemed to be a variation of a backtracking problem. 
    
    Programming Language Used: Python
    
    Directories and Files: + dir ; - file
        +bin
          -executable
          +SeatingAlg
            -main.py
            +lib
              -Theater.py
              +Tests
              
    My Assumptions (in addition to the above assumptions) :    
        -People in a group prefer to seat together - highest priority
        -The further away from the screen, the better the movie experience - next priority
        -Number of reservation requests is less than number of seats available in the theater
        
    Building The Solutions
        -Fork and Clone this Repository
        -To run on the command line, type: bin/SeatAssignment sample-input.txt



