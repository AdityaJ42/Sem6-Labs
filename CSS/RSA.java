// RSA Algorithm
import java.util.*;
import java.lang.Math;

class RSA{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		double p, q, e, phi, n;
		double d, m = 0.0;
		double ct;
		System.out.print("Enter the message to be encrypted: ");
		m = sc.nextDouble();
		
		System.out.print("Enter the values of p, q, e: ");
		p = sc.nextDouble();
		q = sc.nextDouble();
		e = sc.nextDouble();
		n = p * q;
		phi = (p - 1) * (q - 1);
		d = (2 * phi + 1) / e;

		ct = Math.pow(m, e) % n;
		double decrypted = Math.pow(ct, d) % n;

		System.out.println("Public Key: " + n + ", " + e);
		System.out.println("Private Key: " + d);
		System.out.println("Message: " + m);
		System.out.println("Encrypted Text: " + ct);
	}
}