import sys
import pygame

from alien import Alien
from bullet import Bullet
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()


def check_keyup_events(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)  # checks if x_y of mouse inside the button
    if button_clicked and not stats.game_active:
        # Resets game settings
        stats.reset_stats()
        ai_settings.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)  # Makes cursor invisible after clicking play
        stats.game_active = True

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)

        ship.center_ship()


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
            add_delete_bullet(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1

        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


# Code about bullets
def add_delete_bullet(event, ai_settings, screen, ship, bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            if len(bullets) < ai_settings.bullets_allowed:
                new_bullet = Bullet(ai_settings, screen, ship)
                bullets.add(new_bullet)


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update(ai_settings)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collision_baliens(ai_settings, screen, stats, sb, ship, aliens, bullets)


def update_fleet(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collision_baliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
    new_fleet(ai_settings, screen, ship, aliens, bullets)


def collision_baliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)  # SuperBullets, may be used!
    if collisions:
        stats.score += ai_settings.alien_points
        sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()

        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


# Down is code about creating aliens

def get_number_alien_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))  # We don't know alien_width, it's a float, so int() it
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x

    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)

    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def new_fleet(ai_settings, screen, ship, aliens, bullets):
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):  # This method gets sprite and group!
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
        check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)


# Main update function that summarize all on the screen
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    if not stats.game_active:
        play_button.draw_button()
        pygame.display.flip()
    else:
        screen.fill(ai_settings.bg_color)
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        sb.show_score()
        ship.blitme()
        aliens.draw(screen)

    pygame.display.flip()


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
