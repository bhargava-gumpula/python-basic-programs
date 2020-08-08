import pickle
l = [1,2,3,4,5,6,7,8,9,10]
save_file = open('save_dat', 'wb')
pickle.dump(l,save_file)
save_file.close()




