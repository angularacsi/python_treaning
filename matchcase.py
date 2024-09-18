def error_check(status):
    
    match status:
        case 'success':
            return 'Operation Successful'
        case 'error':
            return 'An error occurred'
        case 'warning':
            return 'Warning occurred'
        case 'info':
            return 'Informational message'
        case _:
            return 'Invalid status'
    
print(error_check('error'))