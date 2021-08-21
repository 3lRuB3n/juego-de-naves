namespace SpriteKind {
    export const Punto = SpriteKind.create()
}
let Muerte: Sprite = null
let mySprite: Sprite = null
let Enemigo: Sprite = null
let Projectile1: Sprite = null
let projectile2: Sprite = null
function CreaPersonaje () {
    Muerte = sprites.create(img`
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
        `, SpriteKind.Punto)
    info.setLife(3)
    mySprite = sprites.create(assets.image`Nave Espacial 1`, SpriteKind.Player)
    mySprite.setPosition(scene.screenWidth() / 2, 105)
    controller.moveSprite(mySprite, 130, 0)
    animation.runImageAnimation(
    mySprite,
    assets.animation`Animación Nave 1`,
    300,
    true
    )
}
function CreaMundo () {
    effects.starField.startScreenEffect()
    scene.setBackgroundColor(15)
}
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    otherSprite.startEffect(effects.spray, 1000)
    info.changeLifeBy(-1)
    sprite.destroy()
})
info.onLifeZero(function () {
    mySprite.startEffect(effects.spray)
    mySprite.follow(Muerte, 25)
    pause(600)
    mySprite.startEffect(effects.disintegrate)
    pause(5000)
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    false
    )
    pause(500)
    effects.clearParticles(mySprite)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy()
    otherSprite.startEffect(effects.fire)
    info.changeScoreBy(1)
    pause(60)
    otherSprite.destroy()
})
forever(function () {
    if (!(info.life() == 0)) {
        Enemigo = sprites.create(img`
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
            `, SpriteKind.Enemy)
        Enemigo.setPosition(randint(7, 148), -5)
        Enemigo.setVelocity(0, 60)
        animation.runImageAnimation(
        Enemigo,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        450,
        true
        )
        pause(1000)
    }
})
forever(function () {
    while (controller.A.isPressed()) {
        Projectile1 = sprites.createProjectileFromSprite(img`
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
            `, mySprite, 0, -80)
        projectile2 = sprites.createProjectileFromSprite(img`
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
            `, mySprite, 0, -80)
        projectile2.x += 7
        pause(250)
    }
})
