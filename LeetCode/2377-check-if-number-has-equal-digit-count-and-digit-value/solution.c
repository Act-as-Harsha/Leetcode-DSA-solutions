bool digitCount(char* num) 
{
int n = strlen(num);
int table[10] = {0}; 
int i;
for (i = 0; i < n; i++) 
{
table[num[i] - '0']++;
}
for (i = 0; i < n; i++) 
{
if (table[i] != (num[i] - '0')) 
{
return false;
}
} 
return true;
}
