// Brute Force Decryption for substitution cipher
import java.util.*;

class DecryptBruteForce{
	public static String decrypt(String m, int k){
		String decrypted = "";
		for(int i = 0; i < m.length(); i++){
			int temp = (int)(m.charAt(i));
			if(temp >= 65 && temp <= 90){
				temp = (temp - 65) % 26;
				if(temp - k < 0)
					temp = temp - k + 26;
				else
					temp = temp - k;
				decrypted += (char)(temp % 26 + 65);
			}
			else if(temp >= 97 && temp <= 122){
				temp = (temp - 97) % 26;
				if(temp - k < 0)
					temp = temp - k + 26;
				else
					temp = temp - k;
				decrypted += (char)(temp % 26 + 97);
			}
		}

		return decrypted;
	}

	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		String msg, ct;
		System.out.print("Enter the message to be decrypted: ");
		ct = sc.nextLine();
		for(int i = 1; i <= 26; i++){
			msg = decrypt(ct, i);
			System.out.println("Key: " + i + " Message: " + msg);
		}
	}
}