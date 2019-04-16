import java.io.*;
import java.util.*;
import java.lang.*;
public class ICG{

	private static final char[][] precedence = { 
		{'/', '1'}, 
		{'*', '1'}, 
		{'+', '2'}, 
		{'-', '2'} 
	}; 
 	private static int precedenceOf(String t) 
	{ 
		char token = t.charAt(0); 
		for (int i=0; i < precedence.length; i++) 
		{ 
			if (token == precedence[i][0]) 
			{ 
				return Integer.parseInt(precedence[i][1]+""); 
			} 
		} 
		return -1; 
	} 
	public static String re(String eq,int i,String tr)
	{
	int mid=eq.indexOf(tr);
	String ne="",toFind="";
	if(!(eq.charAt(mid-2)=='t')&&!(eq.charAt(mid+1)=='t'))
		{
				toFind=eq.substring(mid-1,mid+2);
				ne=eq.substring(0,mid-1)+"t"+Integer.toString(i)+eq.substring(mid+2,eq.length());
		}	
		else if(eq.charAt(mid-2)=='t')
		{
			 if(eq.charAt(mid+1)=='t')
			 {
				toFind=eq.substring(mid-2,mid+3);
				ne=eq.substring(0,mid-2)+"t"+Integer.toString(i)+eq.substring(mid+3,eq.length());				
			 }
			else{
				toFind=eq.substring(mid-2,mid+2);
				ne=eq.substring(0,mid-2)+"t"+Integer.toString(i)+eq.substring(mid+2,eq.length());
			    }
		}
		else
		{
			toFind=eq.substring(mid-1,mid+3);
			ne=eq.substring(0,mid-1)+"t"+Integer.toString(i)+eq.substring(mid+3,eq.length());
		}
		System.out.println("t"+i+"="+toFind);
		return ne;					
	}
	public static void assignment(String e)
	{
	int i=1;
	while(e.contains("^")||e.contains("*")||e.contains("/")||e.contains("+")||e.contains("-"))
	{
	if(e.contains("^"))
	{
		String toReplace="^";
		int mid=e.lastIndexOf(toReplace);	
		String toFind;
		String ne="";
		if(!(e.charAt(mid-2)=='t')&&!(e.charAt(mid+1)=='t'))
		{
				toFind=e.substring(mid-1,mid+2);
				ne=e.substring(0,mid-1)+"t"+Integer.toString(i)+e.substring(mid+2,e.length());
		}	
		else if(e.charAt(mid-2)=='t')
		{
			 if(e.charAt(mid+1)=='t')
			 {
				toFind=e.substring(mid-2,mid+3);
				ne=e.substring(0,mid-2)+"t"+Integer.toString(i)+e.substring(mid+3,e.length());				
			 }
			else{
				toFind=e.substring(mid-2,mid+2);
				ne=e.substring(0,mid-2)+"t"+Integer.toString(i)+e.substring(mid+2,e.length());
			    }
		}
		else
		{
			toFind=e.substring(mid-1,mid+3);
			ne=e.substring(0,mid-1)+"t"+Integer.toString(i)+e.substring(mid+3,e.length());
		}
		System.out.println("t"+i+"="+toFind);
		e=ne;		
	}
	else if(e.contains("*")||e.contains("/"))
	{
		if(e.contains("*")&&e.contains("/"))			
		{
			if(e.indexOf("*")<e.indexOf("/"))
			{
			String toReplace="*";
			e=re(e,i,toReplace);		
			}
			else
			{
			String toReplace="/";
			e=re(e,i,toReplace);	
			}		
		}
		else if(e.contains("*"))
		{
			String toReplace="*";
			e=re(e,i,toReplace);			
		}
		else
		{
			String toReplace="/";
			e=re(e,i,toReplace);	
		}
	}
	else
	{
		if(e.contains("+")&&e.contains("-"))			
		{
			if(e.indexOf("+")<e.indexOf("-"))
			{
			String toReplace="+";
			e=re(e,i,toReplace);		
			}
			else
			{
			String toReplace="-";
			e=re(e,i,toReplace);	
			}		
		}
		else if(e.contains("+"))
		{
			String toReplace="+";
			e=re(e,i,toReplace);			
		}
		else
		{
			String toReplace="-";
			e=re(e,i,toReplace);	
		}
	}
	System.out.println(e);
	i=i+1;
	}
	}
	public static void relational(String equation)
	{
		int index=100,total=0;
		int [] Count=new int[5];
		for (int i=0;i<5;i++)
			Count[i]=0;
		while(equation.contains("&&")||equation.contains("||"))
		{
			String operand = equation.substring(3,5);
			if(operand.equals("&&"))
				Count[total]=1;
			total=total+1;
			equation=equation.substring(5,equation.length());
			index=getIndex(index,equation,total);	
		}	
		total=total+1;
		index=getIndex(index,equation,total);
		int Conditions=total;
		for (int i=0;i<Conditions-1;i++)
		{
			total=total+1;
			if(Count[i]==1)
				System.out.println(Integer.toString(index)+" :t"+Integer.toString(total)+" =t"+Integer.toString(i+1)+" and t"+Integer.toString(i+2));
			else 	System.out.println(Integer.toString(index)+" :t"+Integer.toString(total)+" =t"+Integer.toString(i+1)+" or t"+Integer.toString(i+2));
	index++;
		}
	}
	public static void arithmetic(String expr)
	{
	int i,j,opc=0;
	char token; 
	boolean processed[]; 
	BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	String[][] operators = new String[10][2]; 
	String  temp;
	processed = new boolean[expr.length()]; 
	for (i=0; i < processed.length; i++)  
		processed[i] = false;  
	for (i=0; i < expr.length(); i++) 
	{ 
		token = expr.charAt(i); 
		for (j=0; j < precedence.length; j++) 
		{ 
			if (token==precedence[j][0]) 
			{ 
					operators[opc][0] = token+""; 
					operators[opc][1] = i+""; 
					opc++; 
					break; 
			} 
			} 
		} 
		for (i=opc-1; i >= 0; i--) 
		{ 
			for (j=0; j < i; j++) 
			{ 
				if (precedenceOf(operators[j][0]) > precedenceOf(operators[j+1][0])) 
				{ 
					temp = operators[j][0]; 
					operators[j][0] = operators[j+1][0]; 
					operators[j+1][0] = temp; 
					temp = operators[j][1]; 
					operators[j][1] = operators[j+1][1]; 
					operators[j+1][1] = temp; 
				}				 
			} 
		} 
		for (i=0; i < opc; i++) 
		{ 
			j = Integer.parseInt(operators[i][1]+""); 
			String op1="", op2=""; 
			if (processed[j-1]==true) 
			{ 	if (precedenceOf(operators[i-1][0]) == precedenceOf(operators[i][0])) 
				op1 = "t"+i;  
				else 
				{ 	for (int x=0; x < opc; x++) 
						if ((j-2) == Integer.parseInt(operators[x][1]))  
							op1 = "t"+(x+1)+""; 
				} 
			} 
			else 	op1 = expr.charAt(j-1)+""; 
			if (processed[j+1]==true) 
			{ 
				for (int x=0; x < opc; x++) 
				if ((j+2) == Integer.parseInt(operators[x][1])) 
						op2 = "t"+(x+1)+""; 		
			} 
			else 
			op2 = expr.charAt(j+1)+""; 
			System.out.println("t"+(i+1)+" = "+op1+operators[i][0]+op2); 
			processed[j] = processed[j-1] = processed[j+1] = true; 
		}
	}
	public static int getIndex(int index,String equation , int total)
	{
	String condition=equation.substring(0,3);
	System.out.println(Integer.toString(index)+" :if "+condition+" go to "+Integer.toString(index+3));
	index=index+1;
	System.out.println(Integer.toString(index)+" :t"+Integer.toString(total)+"=1");
	index++;
	System.out.println(Integer.toString(index)+" :go to "+Integer.toString(index+2));
	index++;
	System.out.println(Integer.toString(index)+" :t"+Integer.toString(total)+"=0");
	index++;
	return index;
	}
	public static void main(String args[]) throws Exception
	{
	int i,ch,j,l,addr=100; 
	BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	String[][] operators = new String[10][2]; 
	Scanner sc = new Scanner(System.in); 
	String exp,exp1,exp2,exp4;
	while(true)
	{
	System.out.println("1.Assignment 2.Arithmetic 3.Relational");
	ch=sc.nextInt();
	switch(ch)
	{
	case 1:System.out.println("Enter expression");
	       exp=sc.next();
	       assignment(exp);
	break;
	case 2:System.out.println("Enter expression");
	       exp4=in.readLine(); 
	       arithmetic(exp4);
	break;	
	case 3:System.out.println("Enter expression");
	       String equation=sc.next();			
	       relational(equation);		
	break;
	}
}
}
}
