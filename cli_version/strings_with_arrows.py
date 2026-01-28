def string_with_arrows(text, pos_start, pos_end):
    result = ''

    # حساب الفهارس
    idx_start = max(text.rfind('\n', 0, pos_start.idx), 0)
    idx_end = text.find('\n', idx_start + 1)
    if idx_end < 0: idx_end = len(text)
    
    # إنشاء كل سطر
    line_count = pos_end.ln - pos_start.ln + 1
    for i in range(line_count):
        # حساب أعمدة السطر
        line = text[idx_start:idx_end]
        col_start = pos_start.col if i == 0 else 0
        col_end = pos_end.col if i == line_count - 1 else len(line) - 1

        # إضافة إلى النتيجة
        result += line + '\n'
        result += ' ' * col_start + '^' * (col_end - col_start)

        # إعادة حساب الفهارس
        idx_start = idx_end
        idx_end = text.find('\n', idx_start + 1)
        if idx_end < 0: idx_end = len(text)

    return result.replace('\t', '')
