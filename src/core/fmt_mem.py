def memory_format(size, m_type='gb'):
    if m_type == 'kb':
        fmt_memory = size / 1024
        return round(fmt_memory, 2)
    elif m_type == 'mb':
        fmt_memory = size / 1024 / 1024
        return round(fmt_memory, 2)
    elif m_type == 'gb':
        fmt_memory = size / 1024 / 1024 / 1024
        return round(fmt_memory, 2)
    else:
        return f'Unknown memory type - {m_type}'
