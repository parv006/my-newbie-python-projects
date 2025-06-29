import random

# create a list displaying all the tic tac toe lines
#an option to count the scores of players if they decide to replay in loop
print('  ')
print('  ')
print('  ')
print('do you want to play tic tac toe ?')
print('  ')
a=int(input('''          1. yes
          2. no(exit)  '''))
print('  ')
print('  ')

if a==1:
    
    l1=['  ','|','  ','|','  ']
    l2=['___________']
    l3=['  ','|','  ','|','  ']
    l4=['___________']
    l5=['  ','|','  ','|','  ']

    rules_check=(input('''Here is some "general" info about the game and notation:
                          |
                          |    1. position names of matrix : tl|tm|tr          
                          |                                 ________         
                          |                                 ml|mm|mr 
                          |                                 ________
                          |                                 bl|bm|br                                                              
                          |   2.abbrviations : tl: top left
                          |                    tm: top middle
                          |                    tr: top right
                          |                    ml: middle left
                          |                    mm: middle middle
                          |                    mr: middle right
                          |                    bl: bottom left
                          |                    bm: bottom middle
                          |                    br: bottom right
                          |
                          |   3. only 'X' (capital and small for both) and 'O' are allowed ,
                          |      anything else as input will end the
                          |      game and
                          |         other persom is declared as winner 
                          |    
                          |
                          |   press enter if u read the info :    '''))
    if rules_check==9:
        print(' ')
    else:
        print(' ')    

    tl,tm,tr,ml,mm,mr,bl,bm,br ='  ','  ','  ','  ','  ','  ','  ','  ','  ' # type: ignore
    
    r1=['           ' , tl , ' | ' , tm , '| ' , tr ]
    r2=['          ' , l2[0]]
    r3=['           ' , ml , ' | ' , mm , '| ' , mr] 
    r4=['          ' , l4[0]]
    r5=['           ' , bl , ' | ' , bm , '| ' , br]
   
     
    print('  ')
    print('  ')
    print('  ')

    b=int(input('''select the difficulty level: 
            1. 2 player
            2. easy(with bot)
            3. hard(with bot)''')) 
    if b==1:
        r1=['           ' , tl , ' | ' , tm , '| ' , tr ]
        r2=['          ' , l2[0]]
        r3=['           ' , ml , ' | ' , mm , '| ' , mr] 
        r4=['          ' , l4[0]]
        r5=['           ' , bl , ' | ' , bm , '| ' , br]
        print('you have chosen 2 player mode')
        c=input('enter player 1 name: ')
        d=input('enter player 2 name: ')
        print(c + '   VS   ' + d)

        print('  ')
        print('_______GAME STARTS_______')

        print('  ')
        print('  ')
        li1=[c,d]
        

        def move(i):
          mi=input('X OR O')
       
          while True :
           p1=input('read info point 1,2 and enter the position accordingly: ')

           if p1=='tl':
            r1[1]=' ' + mi
            break
           elif p1=='tm':
            r1[3]=' ' + mi
            break  
           elif p1=='tr':
            r1[5]=' ' + mi
            break 
           elif p1=='ml': 
            r3[1]=' ' + mi
            break
           elif p1=='mm': 
            r3[3]=' ' + mi
            break
           elif p1=='mr': 
            r3[5]=' ' + mi
            break
           elif p1=='bl': 
            r5[1]=' ' + mi
            break
           elif p1=='bm':    
            r5[3]=' ' + mi
            break
           elif p1=='br': 
            r5[5]=' ' + mi
            break
           else: 
            print('you have entered a wrong notation')  
            continue  


          print(r1[0]+r1[1]+r1[2]+r1[3]+r1[4]+r1[5])
          print(' ' + r2[0]+r2[1])
          print(r3[0]+r3[1]+r3[2]+r3[3]+r3[4]+r3[5])
          print(' ' + r4[0]+r4[1])
          print(r5[0]+r5[1]+r5[2]+r5[3]+r5[4]+r5[5])
        
        
        while True: 
          print(' ') 
             
          while True:
                  print( c + ' turn: ')
                  m1=input('X OR O')
       
                  while True :
                      p1=input('read info point 1,2 and enter the position accordingly: ')

                      if p1=='tl':
                        r1[1]=' ' + m1
                        break
                      elif p1=='tm':
                        r1[3]=' ' + m1
                        break  
                      elif p1=='tr':
                        r1[5]=' ' + m1
                        break 
                      elif p1=='ml': 
                        r3[1]=' ' + m1
                        break
                      elif p1=='mm': 
                        r3[3]=' ' + m1
                        break
                      elif p1=='mr': 
                        r3[5]=' ' + m1
                        break
                      elif p1=='bl': 
                        r5[1]=' ' + m1
                        break
                      elif p1=='bm':    
                        r5[3]=' ' + m1
                        break
                      elif p1=='br': 
                        r5[5]=' ' + m1
                        break
                      else: 
                        print('you have entered a wrong notation')  



                  print(r1[0]+r1[1]+r1[2]+r1[3]+r1[4]+r1[5])
                  print(' ' + r2[0]+r2[1])
                  print(r3[0]+r3[1]+r3[2]+r3[3]+r3[4]+r3[5])
                  print(' ' + r4[0]+r4[1])
                  print(r5[0]+r5[1]+r5[2]+r5[3]+r5[4]+r5[5])  
              

        
                  print( d + ' turn:  ')
                  m2=input('X OR O')
       
                  while True :
                       p1=input('read info point 1,2 and enter the position accordingly: ')

                       if p1=='tl':
                        r1[1]=' ' + m2
                        break
                       elif p1=='tm':
                        r1[3]=' ' + m2
                        break  
                       elif p1=='tr':
                        r1[5]=' ' + m2
                        break 
                       elif p1=='ml': 
                        r3[1]=' ' + m2
                        break
                       elif p1=='mm': 
                        r3[3]=' ' + m2
                        break
                       elif p1=='mr': 
                        r3[5]=' ' + m2
                        break
                       elif p1=='bl': 
                        r5[1]=' ' + m2
                        break
                       elif p1=='bm':    
                        r5[3]=' ' + m2
                        break
                       elif p1=='br': 
                        r5[5]=' ' + m2
                        break
                       else: 
                        print('you have entered a wrong notation')  
                  print(r1[0]+r1[1]+r1[2]+r1[3]+r1[4]+r1[5])
                  print(' ' + r2[0]+r2[1])
                  print(r3[0]+r3[1]+r3[2]+r3[3]+r3[4]+r3[5])
                  print(' ' + r4[0]+r4[1])
                  print(r5[0]+r5[1]+r5[2]+r5[3]+r5[4]+r5[5])                         
              

                  print( c + ' turn: ')
                  move(3)

                  print( d + ' turn: ')
                  move(4)

                  print( c + ' turn: ')
                  move(5)
                  
                  def check_win(player):
    # Rows
                   if (tl == tm == tr == player) or (ml == mm == mr == player) or (bl == bm == br == player):
                     return True
    # Columns
                   if (tl == ml == bl == player) or (tm == mm == bm == player) or (tr == mr == br == player):
                      return True
    # Diagonals
                   if (tl == mm == br == player) or (tr == mm == bl == player):
                       return True
                   return False
                  
                         

                  print( d + ' turn: ')
                  move(6)
                 


                     


                  print( c + ' turn: ')
                  move(7)
                  if r1[1]==r1[3]==r1[5]==m1 or r3[1]==r3[3]==r3[5]==m1 or r5[1]==r5[1]==r5[1]==m1 or r1[1]==r3[1]==r5[1]==m1 or r1[3]==r3[3]==r5[3]==m1 or r1[5]==r3[5]==r5[5]==m1 or r1[1]==r3[3]==r5[5]==m1 or r1[5]==r3[3]==r5[1]==m1:
                 
                    print('____CONGRATS____' + c + '__YOU___WON!!!__')
                    break
                  
                  elif r1[1]==r1[3]==r1[5]==m1 or r3[1]==r3[3]==r3[5]==m1 or r5[1]==r5[1]==r5[1]==m1 or r1[1]==r3[1]==r5[1]==m1 or r1[3]==r3[3]==r5[3]==m1 or r1[5]==r3[5]==r5[5]==m1 or r1[1]==r3[3]==r5[5]==m1 or r1[5]==r3[3]==r5[1]==m1:
                    print('____CONGRATS____' + d + '__YOU___WON!!!__')
                    break
                     
                  else :
                    print()
                  print( d + ' turn: ')
                  move(8)
                  if r1[1]==r1[3]==r1[5]==m1 or r3[1]==r3[3]==r3[5]==m1 or r5[1]==r5[1]==r5[1]==m1 or r1[1]==r3[1]==r5[1]==m1 or r1[3]==r3[3]==r5[3]==m1 or r1[5]==r3[5]==r5[5]==m1 or r1[1]==r3[3]==r5[5]==m1 or r1[5]==r3[3]==r5[1]==m1:
                 
                    print('____CONGRATS____' + c + '__YOU___WON!!!__')
                    break
                  
                  elif r1[1]==r1[3]==r1[5]==m1 or r3[1]==r3[3]==r3[5]==m1 or r5[1]==r5[1]==r5[1]==m1 or r1[1]==r3[1]==r5[1]==m1 or r1[3]==r3[3]==r5[3]==m1 or r1[5]==r3[5]==r5[5]==m1 or r1[1]==r3[3]==r5[5]==m1 or r1[5]==r3[3]==r5[1]==m1:
                    print('____CONGRATS____' + d + '__YOU___WON!!!__')
                    break

                  else :
                    print()

                  print( c + ' turn: ')
                  move(9)         
                  if r1[1]==r1[3]==r1[5]==m1 or r3[1]==r3[3]==r3[5]==m1 or r5[1]==r5[1]==r5[1]==m1 or r1[1]==r3[1]==r5[1]==m1 or r1[3]==r3[3]==r5[3]==m1 or r1[5]==r3[5]==r5[5]==m1 or r1[1]==r3[3]==r5[5]==m1 or r1[5]==r3[3]==r5[1]==m1:
                 
                    print('____CONGRATS____' + c + '__YOU___WON!!!__')
                    break
                  
                  elif r1[1]==r1[3]==r1[5]==m1 or r3[1]==r3[3]==r3[5]==m1 or r5[1]==r5[1]==r5[1]==m1 or r1[1]==r3[1]==r5[1]==m1 or r1[3]==r3[3]==r5[3]==m1 or r1[5]==r3[5]==r5[5]==m1 or r1[1]==r3[3]==r5[5]==m1 or r1[5]==r3[3]==r5[1]==m1:
                    print('____CONGRATS____' + d + '__YOU___WON!!!__')
                    break
                     
                  else :
                    print()

                  e=int(input('''do you want to play another round?
                         1. yes
                         2. no(exit) '''))
          if e==1:
              print('')
          elif e==2:
            break 
          else:
            print('please enter 1 or 2 ')   

            
               
          
           
           













































































