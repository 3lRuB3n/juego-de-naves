@namespace
class SpriteKind:
    Punto = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    otherSprite.start_effect(effects.spray, 1000)
    info.change_life_by(-1)
    sprite.destroy()
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_life_zero():
    mySprite.start_effect(effects.spray)
    mySprite.follow(Muerte, 25)
    pause(600)
    mySprite.start_effect(effects.disintegrate)
    pause(5000)
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . 2 2 . . . . . . . .
                        . . . . . . 2 5 2 . . . . . . .
                        . . 2 2 . . 2 5 2 . . 2 2 . . .
                        . . 2 5 2 . 2 5 2 4 2 5 2 . . .
                        . . . 2 5 2 2 1 2 4 5 2 . . . .
                        2 2 2 2 4 5 2 1 5 5 2 . . . . .
                        2 5 5 5 5 5 5 1 1 2 2 2 2 2 2 2
                        . 2 2 2 4 2 1 1 1 1 5 5 5 5 5 2
                        . . . . . 4 5 1 5 2 2 4 2 2 2 .
                        . . . . 2 5 2 1 2 5 4 . . . . .
                        . . . 2 5 2 4 5 2 2 5 2 . . . .
                        . . 2 5 2 . 4 5 2 . 2 5 2 . . .
                        . . 2 2 . . 2 5 2 . . 2 2 . . .
                        . . . . . . 2 5 2 . . . . . . .
                        . . . . . . 2 5 2 . . . . . . .
                        . . . . . . 2 2 . . . . . . . .
            """),
            img("""
                . . 4 4 . . . 4 4 . . . . . . .
                        . 4 5 5 2 . . 4 5 4 . . 4 4 4 .
                        . 4 5 5 2 . . 4 5 4 . 4 5 5 4 .
                        . . 4 2 2 . . 2 5 2 . 2 5 5 4 .
                        . 4 4 . . . . . 2 2 . 2 2 2 . .
                        4 5 5 2 2 . . . . . . . 4 4 . .
                        4 5 5 5 2 . . . . . . 2 5 5 4 4
                        4 5 5 2 . . . . . . 4 5 5 5 5 4
                        . 4 2 2 . . . . . . . 2 5 5 4 .
                        . . . . . . . 2 . . . . 4 4 . .
                        . . 2 2 2 . 2 5 2 . . 2 2 2 . .
                        . 4 5 5 2 2 4 5 5 2 . 2 5 5 4 4
                        4 5 5 5 2 2 5 5 5 2 . 2 5 5 5 4
                        4 5 5 4 . . 4 5 4 . . . 4 5 5 4
                        4 4 4 . . . . 4 4 . . . . 4 4 .
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . 2 5 2 . . . .
                        . . . . 2 5 2 . . 2 5 5 2 . . .
                        . . . 2 5 5 2 . . . 2 5 2 . . .
                        . . . 2 5 2 . 2 5 2 . 2 . . . .
                        . . . . 2 . . 2 5 2 . . . . . .
                        2 5 2 . . . . . 2 . . 2 5 2 . .
                        5 5 2 . . . . . . . . 2 5 5 2 .
                        5 2 . . . . . . . . . . 2 5 2 .
                        2 . . . . . . . . . . . . 2 . .
                        . . 2 5 2 . 2 5 2 . . . 2 5 2 .
                        . 2 5 5 2 . 2 5 2 . . . 2 5 5 2
                        . 2 5 2 . . 2 5 2 . . . . 2 5 2
                        . . 2 . . . . 2 . . . . . . 2 .
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
            """)],
        500,
        False)
    pause(500)
    effects.clear_particles(mySprite)
info.on_life_zero(on_life_zero)

def on_on_overlap2(sprite, otherSprite):
    sprite.destroy()
    otherSprite.start_effect(effects.fire)
    info.change_score_by(1)
    pause(60)
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

projectile2: Sprite = None
Projectile1: Sprite = None
Enemigo: Sprite = None
mySprite: Sprite = None
Muerte: Sprite = None
Muerte = sprites.create(img("""
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    """),
    SpriteKind.Punto)
info.set_life(0)
effects.star_field.start_screen_effect()
mySprite = sprites.create(assets.image("""
    Nave Espacial 1
"""), SpriteKind.player)
mySprite.set_position(scene.screen_width() / 2, 105)
controller.move_sprite(mySprite, 130, 0)
scene.set_background_color(15)
animation.run_image_animation(mySprite,
    assets.animation("""
        Animación Nave
    """),
    300,
    True)

def on_forever():
    global Enemigo
    if not (info.life() == 0):
        Enemigo = sprites.create(img("""
                . . . . . . . . . c c 8 . . . .
                            . . . . . . 8 c c c f 8 c c . .
                            . . . c c 8 8 f c a f f f c c .
                            . . c c c f f f c a a f f c c c
                            8 c c c f f f f c c a a c 8 c c
                            c c c b f f f 8 a c c a a a c c
                            c a a b b 8 a b c c c c c c c c
                            a f c a a b b a c c c c c f f c
                            a 8 f c a a c c a c a c f f f c
                            c a 8 a a c c c c a a f f f 8 a
                            . a c a a c f f a a b 8 f f c a
                            . . c c b a f f f a b b c c 6 c
                            . . . c b b a f f 6 6 a b 6 c .
                            . . . c c b b b 6 6 a c c c c .
                            . . . . c c a b b c c c . . . .
                            . . . . . c c c c c c . . . . .
            """),
            SpriteKind.enemy)
        Enemigo.set_position(randint(7, 148), -5)
        Enemigo.set_velocity(0, 60)
        animation.run_image_animation(Enemigo,
            [img("""
                    . . . . . . . . . c c 8 . . . .
                                . . . . . . 8 c c c f 8 c c . .
                                . . . c c 8 8 f c a f f f c c .
                                . . c c c f f f c a a f f c c c
                                8 c c c f f f f c c a a c 8 c c
                                c c c b f f f 8 a c c a a a c c
                                c a a b b 8 a b c c c c c c c c
                                a f c a a b b a c c c c c f f c
                                a 8 f c a a c c a c a c f f f c
                                c a 8 a a c c c c a a f f f 8 a
                                . a c a a c f f a a b 8 f f c a
                                . . c c b a f f f a b b c c 6 c
                                . . . c b b a f f 6 6 a b 6 c .
                                . . . c c b b b 6 6 a c c c c .
                                . . . . c c a b b c c c . . . .
                                . . . . . c c c c c c . . . . .
                """),
                img("""
                    . . . c c c c c c a a c . . . .
                                . . c c c c c f f 8 c 6 c c . .
                                . c c c 8 a c f f f f c 6 c . .
                                . c f f c a c c f f f c b c . .
                                8 8 f f a a c c c f 8 b a c c .
                                c f f a a c c c a a b b 6 a c c
                                c c a a c c c c c a a a 6 6 c c
                                . c c c c a c c a c a f f 6 b c
                                . c f f f 8 b a c c f f f b b c
                                . 8 8 f f f a b c c f f a b a c
                                . . 8 f f f 8 b a c c a b b c c
                                . . c c f f b a a a a b b c c .
                                . . c c c b b a c a a c c c . .
                                . . . c c c a c f 8 c c . . . .
                                . . . . c c a f 8 a a . . . . .
                                . . . . 8 c c a a c . . . . . .
                """),
                img("""
                    . . . . . c c c c c c . . . . .
                                . . . . c c c b b a c c . . . .
                                . c c c c a 6 6 b b b c c . . .
                                . c 6 b a 6 6 f f a b b c . . .
                                c 6 c c b b a f f f a b c c . .
                                a c f f 8 b a a f f c a a c a .
                                a 8 f f f a a c c c c a a 8 a c
                                c f f f c a c a c c a a c f 8 a
                                c f f c c c c c a b b a a c f a
                                c c c c c c c c b a 8 b b a a c
                                c c a a a c c a 8 f f f b c c c
                                c c 8 c a a c c f f f f c c c 8
                                c c c f f a a c f f f c c c . .
                                . c c f f f a c f 8 8 c c . . .
                                . . c c 8 f c c c 8 . . . . . .
                                . . . . 8 c c . . . . . . . . .
                """),
                img("""
                    . . . . . . c a a c c 8 . . . .
                                . . . . . a a 8 f a c c . . . .
                                . . . . c c 8 f c a c c c . . .
                                . . c c c a a c a b b c c c . .
                                . c c b b a a a a b f f c c . .
                                c c b b a c c a b 8 f f f 8 . .
                                c a b a f f c c b a f f f 8 8 .
                                c b b f f f c c a b 8 f f f c .
                                c b 6 f f a c a c c a c c c c .
                                c c 6 6 a a a c c c c c a a c c
                                c c a 6 b b a a c c c a a f f c
                                . c c a b 8 f c c c a a f f 8 8
                                . . c b c f f f c c a c f f c .
                                . . c 6 c f f f f c a 8 c c c .
                                . . c c 6 c 8 f f c c c c c . .
                                . . . . c a a c c c c c c . . .
                """)],
            450,
            True)
        pause(1000)
forever(on_forever)

def on_forever2():
    global Projectile1, projectile2
    while controller.A.is_pressed():
        Projectile1 = sprites.create_projectile_from_sprite(img("""
                . . . 4 4 4 . . . . . . . . . .
                            . . 4 4 5 4 4 . . . . . . . . .
                            . . 2 5 5 5 2 . . . . . . . . .
                            . . 2 5 5 5 2 . . . . . . . . .
                            . . . 2 5 2 . . . . . . . . . .
                            . . . 2 5 2 . . . . . . . . . .
                            . . . . 2 . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            0,
            -80)
        projectile2 = sprites.create_projectile_from_sprite(img("""
                . . . 4 4 4 . . . . . . . . . .
                            . . 4 4 5 4 4 . . . . . . . . .
                            . . 2 5 5 5 2 . . . . . . . . .
                            . . 2 5 5 5 2 . . . . . . . . .
                            . . . 2 5 2 . . . . . . . . . .
                            . . . 2 5 2 . . . . . . . . . .
                            . . . . 2 . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            0,
            -80)
        projectile2.x += 7
        pause(250)
forever(on_forever2)