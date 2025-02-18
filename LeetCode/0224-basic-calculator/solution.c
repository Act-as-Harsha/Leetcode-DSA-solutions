int calc(char **s)
{
    int result = 0;
    short minus = 1;
    while (**s != 0 && **s != ')') {

        if (isdigit(**s)) {
            result += minus * strtol(*s, &*s, 10);
            minus *= minus;
            (*s)--; 
        }
        else if (**s == '(') {
            (*s)++; 
            result += minus * calc(s);
            minus *= minus;
        }
        else if (**s == '-') minus = -1;

        (*s)++;
    }
    return result;
}

int calculate(char* s) {return calc(&s);}
