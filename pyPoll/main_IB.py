import os
import csv
total_votes = 0
candidates_names = ''
Dictionary= {}
vote_count = 0
vote_count_cand=0
election_file = os.path.join("","Resources","election_data.csv")
highest_votes = 0
winner = ''
with open(election_file, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidates_names = row[2]
        
        if not candidates_names in Dictionary:
            Dictionary.update({candidates_names : 1})
        else:
          Dictionary[candidates_names] += 1

        
        
print("Election Results")  
print("--------------------------------------")          
print(" total votes : " + str(total_votes))
print("--------------------------------------") 
votestring="Individual Votes\n"
for key,v in Dictionary.items():
    
    votestring+=((( key) + " : " + "{0:.0f}%".format ((v/total_votes)*100)) + " (" + str(v) + ")" + "\n"  )

    print((( key) + " : " + "{0:.0f}%".format ((v/total_votes)*100)) + " (" + str(v) + ")" )
    if v > highest_votes:
        highest_votes = v
        winner = key
        

        
print("--------------------------------------")          
     
print("winner : " + winner)
    
output_path = os.path.join("", "election_results.txt")
with open(output_path, 'w', newline='') as out:
    out = open(output_path,"w")
    out.write("Election Results\n")  
    out.write("--------------------------------------\n")          
    out.write(" total votes : " + str(total_votes) + "\n")
    out.write(votestring)
    out.write("--------------------------------------\n") 
    out.write("--------------------------------------\n") 
    out.write("winner : " + winner + "\n")
    out.close()

print("Done writing to result file: " + output_path)





