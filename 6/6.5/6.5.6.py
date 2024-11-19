def best_sender(messages, senders):
    from collections import defaultdict
    senders_messages = sorted(list(zip(senders, messages)), key=lambda x: x[0], reverse=True)
    result = defaultdict(int)
    for sender in senders_messages:
        result[sender[0]] += len(sender[1].split())
    '''    
    return result
    '''
    return max(result, key=lambda x: result[x])
