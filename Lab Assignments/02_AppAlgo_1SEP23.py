# Lab 2

def is_rotation(s1, s2, num_rotations):
    # if len(s1)!=len(s2):
    #     return False;
    for i in range(1,num_rotations+1):
        temp = s1[-i:] + s1[:-i];
       # temp2 = s1[i:] + s1[:i];
        #print("temp=",temp);
       # print("temp2=",temp2);
        if temp == s2: #or temp2==s2:
            return True;
    return False;

print(is_rotation("abcdef","cdefab",7));
print(is_rotation("syncopy","opysync",3));
print(is_rotation("syncopy","opysync",4));

print(is_rotation("abcde","eabcd",41));
print(is_rotation("python","npytho",1));
print(is_rotation("rotation","ationrot",4));
