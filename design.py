def print_design(n):
    """
    Generate design pattern based on FORMULAQSOLUTIONS
    Returns a list of lines for the pattern
    """
    base = "FORMULAQSOLUTIONS"
    extended = base * 5 
    lines = []
    
    if n % 2 == 1:
        
        middle = (n + 1) // 2
        max_length = 2 * middle - 1
        total_lines = n
        
        for i in range(1, total_lines + 1):
            if i <= middle:
                length = 2 * i - 1
            else:
                length = 2 * (n - i) + 1
            
            start_pos = i - 1
            substring = extended[start_pos:start_pos + length]
            
            
            spaces = " " * ((max_length - length) // 2)
            lines.append(spaces + substring)
    else:
        
        peak_line = n // 2 + 1
        max_length = 2 * peak_line - 1
        total_lines = n + 1  
        
        for i in range(1, total_lines + 1):
            if i <= peak_line:
                length = 2 * i - 1
            else:
                length = 2 * (total_lines - i) + 1
            
            start_pos = i - 1
            substring = extended[start_pos:start_pos + length]
            
            spaces = " " * ((max_length - length) // 2)
            lines.append(spaces + substring)
    
    return lines

def generate_pattern_response(n):
    """
    Generate complete response including input validation
    """
    try:
        n = int(n)
        n = max(1, min(100, n))  
        
        lines = print_design(n)
        pattern = '\n'.join(lines)
        
        return {
            'success': True,
            'input': n,
            'pattern': pattern,
            'total_lines': len(lines)
        }
    except (ValueError, TypeError):
        return {
            'success': False,
            'error': 'Please enter a valid integer between 1 and 100.'
        }
