#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Nov 29 15:03:39 2016

@author: Esther Nwogu

Assign Seating in a Movie Theater to Customer Reservations
"""
import numpy as np
#import sys
#import random as random

class Theater(object):

    def __init__(self,totalNumRows, totalNumCols, inputFilePath):

        self.totalNumRows = totalNumRows
        self.totalNumCols = totalNumCols 
        self.inputFilePath = inputFilePath  
        self.outputFilePath = 'lib/data/output.txt'            
                                                                                #(10x20) matrix for holding total seats in theater
        self.theaterSeats = np.empty([self.totalNumRows,self.totalNumCols], dtype=object)         
                                                     #empty dictionary        
        self.currentRow = totalNumRows-1                                        #start from top row        
        self.currentCol = 0                                                    #start from first column   
        self.currentReserveNo=''
        self.seatsAvailablePerRow = [20]*10                                     #num seats left per row        
        self.theaterFilled = 0                                                  #theater is not filled  - boolean      
        self.SumOfSeatsRequested = 0                                             #total number of reservations received
        self.reservations = {} 
        self.assignmentResult = {}                                              #empty dictionary
                           
        self.setSeatNames()
#        for i in range(totalNumRows):
#            for j in range(totalNumCols):
#                sys.stdout.write(self.theaterSeats[i][j]+ " ")
#            sys.stdout.write("\n")
#        sys.stdout.flush()
        self.getReservations()             
        

                
    def getReservations(self):   
        with open(self.inputFilePath) as file:                                  #reading data from file into reservations
            for line in file:                
                line = line.strip()                
                reserve_no, num_seats = line.split()                            #get reservation no and seats
                self.reservations[reserve_no] = int(num_seats)                     #populate dictionary: reservations
                self.SumOfSeatsRequested = self.SumOfSeatsRequested + int(num_seats) #sum of seats requested
            #print("totalSeatRequests: "+ str(self.SumOfSeatsRequested))
            #print(self.reservations)
        

    def setSeatNames(self):                                                     #fill values of seats with seat numbers
        #setting the name of seats
        for row in range(self.totalNumRows):
            for col in range (self.totalNumCols):
                rowName = self.getRowName(row)
                colName = str(col + 1)
                self.theaterSeats[row][col] = rowName + colName
                
                       
        
    def getRowName(self, row):                                                  #get letter representation of row
        return chr(65 + row) 
        
        
    def getRowWithEnoughSeats(self, numSeatsRequested):                         #check if all members of a group can be seated in a row
        
        suitableRows = [index for index,seats in enumerate(self.seatsAvailablePerRow) if seats >= numSeatsRequested]
        #print("suitableRows")
        #print(suitableRows)
        if len(suitableRows) == 0:
            return -1
        else:            
            return max(suitableRows)                                            #preference is given to seats further from screen
            
            
    def getNextEmptyColumn(self):   
        start = self.totalNumCols - (self.seatsAvailablePerRow[self.currentRow]) - 1                                            #check for the next empty seat in the row
        for col in range(start, self.totalNumCols):
            if self.theaterSeats[self.currentRow][col] == 'X':                
                pass
            else:
                return col
                
    
    def Assign(self):        
        for reservationNo, seatsRequested in sorted(self.reservations.items()): 
            self.currentReserveNo = reservationNo
            self.assignmentResult[reservationNo] = []                       #empty list of assigned seats for reservation no                                
            self.Reserve(seatsRequested)
        
                   
    def Reserve(self, seatsRequested):
        rowResult = self.getRowWithEnoughSeats(seatsRequested)
        #sys.stdout.write("rowResult: " + str(rowResult) + "\n\n" )       
        if rowResult != -1:
            self.currentRow = rowResult
            self.currentCol = self.getNextEmptyColumn()
            self.ReserveSeats(seatsRequested)
        else:
            #print(seatsRequested)
            self.Reserve(seatsRequested / 2)                
            self.Reserve(seatsRequested - (seatsRequested / 2))
            
        
    def ReserveSeats(self, seatsRequested):
        for index in range(seatsRequested):
            self.assignmentResult[self.currentReserveNo].append(self.theaterSeats[self.currentRow][self.currentCol])
            self.theaterSeats[self.currentRow][self.currentCol] = 'X'
            self.seatsAvailablePerRow[self.currentRow] -= 1
            self.currentCol += 1
            
    
    def DisplayAssignmentResult(self):
        print(self.assignmentResult)
        
        
    def WriteOutputToFile(self):                    
        with open(self.outputFilePath,'w+') as outfile:
            outfile.truncate()
            for reservationNo in sorted(self.assignmentResult):
                outfile.write(reservationNo+','+','.join(self.assignmentResult[reservationNo])+'\n')      
        print("Find result in data/output.txt")
        
       
            
        
