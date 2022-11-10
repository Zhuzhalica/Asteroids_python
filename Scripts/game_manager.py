def in_screen(screen, pos):
    """Находится ли объект в границах экрана по позиции"""
    screen_rect = screen.get_rect()
    return screen_rect.top <= pos.y <= screen_rect.bottom \
           and screen_rect.left <= pos.x <= screen_rect.right
