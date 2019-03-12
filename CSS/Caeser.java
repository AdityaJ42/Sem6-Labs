// Caesar Cipher Algorithm
import java.util.*;

class Caeser{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		String msg, encrypted = "";
		int key;
		System.out.print("Enter the message to be encrypted: ");
		msg = sc.nextLine();
		System.out.print("Enter the key: ");
		key = sc.nextInt();
		for(int i = 0; i < msg.length(); i++){
			int temp = (int)(msg.charAt(i));
			if(temp >= 65 && temp <= 90){
				temp = (temp - 65) % 26;
				encrypted += (char)((temp + key) % 26 + 65);
			}
			else if(temp >= 97 && temp <= 122){
				temp = (temp - 97) % 26;
				encrypted += (char)((temp + key) % 26 + 97);
			}
		}
		System.out.println("The encrypted message is: " + encrypted);
	}
}