import java.util.*;

class Transposition{
	public static void encrypt(String pt, int key[]){
		int rows, cols, count = 0;
		String encrypted = "";
		cols = key.length;
		if(pt.length() % cols == 0)
			rows = pt.length() / cols;
		else
			rows = pt.length() / cols + 1;
		char encryption_matrix[][] = new char[rows][cols];
		for(int i = 0; i < rows; i++){
			for(int j = 0; j < cols; j++){
				if(count == pt.length())
					break;
				char ch = pt.charAt(count++);
				if(ch == ' '){
					--j;
					continue;
				}
				encryption_matrix[i][j] = ch;
			}
		}
		System.out.println("Encryption Matrix:");
		for(int i = 0; i < rows; i++){
			for(int j = 0; j < cols; j++){
				System.out.print(encryption_matrix[i][j] + " ");
			}
			System.out.println();
		}
		for(int i = 0; i < key.length; i++){
			for(int j = 0; j < rows; j++){
				encrypted += encryption_matrix[j][key[i] - 1];
			}
		}
		System.out.println("Encrypted Message: " + encrypted);
	}

	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		String msg;
		int key, j = 0;

		System.out.print("Enter the message to be encrypted: ");
		msg = sc.nextLine();
		System.out.print("Enter the key: ");
		key = sc.nextInt();
		
		String temp = Integer.toString(key);
		int k[] = new int[temp.length()];
		for(int i = 0; i < temp.length(); i++)
			k[j++] = temp.charAt(i) - '0';

		encrypt(msg, k);
	}
}
/*
aditya@aditya-HP-Pavilion-Notebook:~/Desktop/College/CSS$ javac Transposition.java
aditya@aditya-HP-Pavilion-Notebook:~/Desktop/College/CSS$ java Transposition
Enter the message to be encrypted: hello world
Enter the key: 213
Encryption Matrix:
h e l 
l o w 
o r l 
d   
Encrypted Message: eorhlodlwl
*/