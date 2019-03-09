import java.util.*;

class decryptTranspose{
	public static void decrypt(String ct, int key[]){
		int rows, cols, i, j, count = 0, l = ct.length();
		String decrypted = "";
		cols = key.length;

		if(l % cols == 0)
			rows = l / cols;
		else
			rows = (l / cols) + 1;

		char matrix[][] = new char[rows][cols];
		for(i = 0; i < cols; i++){
			for(j = 0; j < rows; j++){
				if(count == l)
					break;
				char temp = ct.charAt(count++);
				matrix[j][key[i] - 1] = temp;
			}
		}

		System.out.println("Decryption Matrix:");
		for(i = 0; i < rows; i++){
			for(j = 0; j < cols; j++){
				System.out.print(matrix[i][j] + " ");
				decrypted += matrix[i][j];
			}
			System.out.println();
		}

		System.out.println("The decrypted message is: " + decrypted);
	}

	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		String ct;
		int key, j = 0;

		System.out.print("Enter the message to be decrypted: ");
		ct = sc.nextLine();
		System.out.print("Enter the key: ");
		key = sc.nextInt();

		String temp = Integer.toString(key);
		int k[] = new int[temp.length()];
		for(int i = 0; i < temp.length(); i++)
			k[j++] = temp.charAt(i) - '0';

		decrypt(ct, k);
	}
}