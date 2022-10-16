class SpriteKindLegacy(Enum):
    Player = 0
    Projectile = 1
    Food = 2
    Enemy = 3
    Spaceship = 4
    AlienShot = 5
    Fortress = 6
def moveAliensDown():
    for value in sprites.all_of_kind(SpriteKindLegacy.Enemy):
        value.y += aliensShiftAmt
        if value.y > scene.screen_height() - value.height / 2:
            game.over(False)
def spawnSpaceship():
    global spaceship
    spaceship = sprites.create(img("""
            . . . . . 2 2 2 2 2 2 . . . . . 
                    . . . 2 2 2 2 2 2 2 2 2 2 . . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
                    . 2 2 f 2 f 2 f f 2 f 2 f 2 2 . 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    . 2 2 2 . . 2 2 2 2 . . 2 2 2 . 
                    . . 2 . . . . . . . . . . 2 . . 
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
        SpriteKindLegacy.Spaceship)
    if Math.percent_chance(50):
        spaceship.set_position(scene.screen_width(), 12)
        spaceship.vx = 0 - spaceshipSpeed
    else:
        spaceship.set_position(0, 12)
        spaceship.vx = spaceshipSpeed
    spaceship.set_flag(SpriteFlag.AUTO_DESTROY, True)

def on_overlap_projectile_spaceship(sprite, otherSprite):
    global destroyedAlien
    sprite.destroy()
    destroyedAlien = otherSprite
    destroyAlien()
sprites.on_overlap(SpriteKindLegacy.Projectile,
    SpriteKindLegacy.Spaceship,
    on_overlap_projectile_spaceship)

def on_overlap_projectile_fortress(sprite2, otherSprite2):
    global struckFortress
    sprite2.destroy()
    struckFortress = otherSprite2
    degradeFortress()
sprites.on_overlap(SpriteKindLegacy.Projectile,
    SpriteKindLegacy.Fortress,
    on_overlap_projectile_fortress)

def on_overlap_alien_shot_player(sprite3, otherSprite3):
    sprite3.destroy()
    destroyPlayer()
sprites.on_overlap(SpriteKindLegacy.AlienShot,
    SpriteKindLegacy.Player,
    on_overlap_alien_shot_player)

def degradeFortress():
    global fortressImage
    fortressImage = struckFortress.image
    if fortressImage.get_pixel(6, 6) == 7:
        struckFortress.set_image(img("""
            c 6 6 . 6 6 c 6 6 . 6 6 c . . . 
                        6 c 6 6 . 6 6 c 6 6 . 6 6 c . . 
                        6 6 c 6 6 . 6 6 c 6 6 . 6 6 c . 
                        . 6 6 c c c c c c c c c c c c c 
                        6 . 6 c . 7 7 7 . c . 7 7 7 . c 
                        6 6 . c 7 . 7 . 7 c 7 . 7 . 7 c 
                        c 6 6 c 7 7 . 7 7 c 7 7 . 7 7 c 
                        6 c 6 c 7 . 7 . 7 c 7 . 7 . 7 c 
                        6 6 c c . 7 7 7 . c . 7 7 7 . c 
                        6 6 6 c c c c c c c c c c c c c 
                        . 6 6 c . 7 7 7 . c . 7 7 7 . c 
                        6 . 6 c 7 . 7 . 7 c 7 . 7 . 7 c 
                        6 6 . c 7 7 . 7 7 c 7 7 . 7 7 c 
                        c 6 6 c 7 . 7 . 7 c 7 . 7 . 7 c 
                        . c 6 c . 7 7 7 . c . 7 7 7 . c 
                        . . c c c c c c c c c c c c c c
        """))
    elif fortressImage.get_pixel(8, 6) == 7:
        struckFortress.set_image(img("""
            c 6 6 . 6 . c 6 6 . 6 . c . . . 
                        6 c 6 6 . 6 6 c 6 6 . 6 6 c . . 
                        6 6 c . 6 . 6 6 c . 6 . 6 6 c . 
                        . 6 . c c c c c c c c c c c c c 
                        6 . 6 c . 7 . 7 . c . 7 . 7 . c 
                        . 6 . c 7 . 7 . 7 c 7 . 7 . 7 c 
                        c 6 6 c . 7 . 7 . c . 7 . 7 . c 
                        6 c 6 c 7 . 7 . 7 c 7 . 7 . 7 c 
                        6 6 c c . 7 . 7 . c . 7 . 7 . c 
                        6 . 6 c c c c c c c c c c c c c 
                        . 6 . c . 7 . 7 . c . 7 . 7 . c 
                        6 . 6 c 7 . 7 . 7 c 7 . 7 . 7 c 
                        . 6 . c . 7 . 7 . c . 7 . 7 . c 
                        c 6 6 c 7 . 7 . 7 c 7 . 7 . 7 c 
                        . c 6 c . 7 . 7 . c . 7 . 7 . c 
                        . . c c c c c c c c c c c c c c
        """))
    elif fortressImage.get_pixel(6, 5) == 7:
        struckFortress.set_image(img("""
            c . 6 . 6 . c . 6 . 6 . c . . . 
                        . c . 6 . 6 . c . 6 . 6 . c . . 
                        6 . c . 6 . 6 . c . 6 . 6 . c . 
                        . 6 . c c c c c c c c c c c c c 
                        6 . 6 c . 7 . 7 . c . 7 . 7 . c 
                        . 6 . c 7 . . . 7 c 7 . . . 7 c 
                        c . 6 c . 7 . 7 . c . 7 . 7 . c 
                        6 c . c 7 . . . 7 c 7 . . . 7 c 
                        . 6 c c . 7 . 7 . c . 7 . 7 . c 
                        6 . 6 c c c c c c c c c c c c c 
                        . 6 . c . 7 . 7 . c . 7 . 7 . c 
                        6 . 6 c 7 . . . 7 c 7 . . . 7 c 
                        . 6 . c . 7 . 7 . c . 7 . 7 . c 
                        c . 6 c 7 . . . 7 c 7 . . . 7 c 
                        . c . c . 7 . 7 . c . 7 . 7 . c 
                        . . c c c c c c c c c c c c c c
        """))
    else:
        struckFortress.destroy(effects.spray, 500)

def on_button_pressed():
    if attractMode == 1:
        startGame()
controller.any_button.on_event(ControllerButtonEvent.PRESSED, on_button_pressed)

def destroyAlien():
    global alienImage, scoreDelta, numAliensCurr, currAlienPause, numAliensNextSpeedup
    alienImage = destroyedAlien.image
    if alienImage.get_pixel(8, 0) == 2:
        scoreDelta = spaceshipScoreIncrement * randint(1, spaceshipMaxIncrements)
    elif alienImage.get_pixel(2, 4) == 15:
        scoreDelta = alienType3Score
    elif alienImage.get_pixel(1, 3) == 15:
        scoreDelta = alienType1Score
    else:
        scoreDelta = alienType2Score
    changeScore()
    destroyedAlien.destroy(effects.spray, 500)
    numAliensCurr = len(sprites.all_of_kind(SpriteKindLegacy.Enemy))
    if numAliensCurr <= numAliensNextSpeedup:
        currAlienPause = currAlienPause / 2
        numAliensNextSpeedup = numAliensNextSpeedup / 2
        # Double heartbeat tempo.
        music.change_tempo_by(music.tempo())

def on_a_pressed():
    if attractMode == 0:
        if noUpdates == 0:
            if playerDestroyed == 0:
                playerShoot()
    else:
        startGame()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def startGame():
    global attractMode, noUpdates
    attractMode = 0
    for value2 in sprites.all_of_kind(SpriteKindLegacy.Enemy):
        value2.destroy()
    initScreen()
    initAliens()
    initSpaceship()
    initPlayer()
    noUpdates = 0

def on_overlap_projectile_alien_shot(sprite4, otherSprite4):
    sprite4.destroy()
    otherSprite4.destroy()
sprites.on_overlap(SpriteKindLegacy.Projectile,
    SpriteKindLegacy.AlienShot,
    on_overlap_projectile_alien_shot)

def on_overlap_player_enemy(sprite5, otherSprite5):
    game.over(False)
sprites.on_overlap(SpriteKindLegacy.Player,
    SpriteKindLegacy.Enemy,
    on_overlap_player_enemy)

def alienShoot():
    global sprite_list, firingAlien, alienShot
    sprite_list = sprites.all_of_kind(SpriteKindLegacy.Enemy)
    for value3 in sprites.all_of_kind(SpriteKindLegacy.Spaceship):
        sprite_list.append(value3)
    if len(sprite_list) > 0:
        firingAlien = sprite_list[randint(0, len(sprite_list) - 1)]
        alienShot = sprites.create(img("""
                . . 1 . 1 . 1 . 
                            . . . 1 1 1 . . 
                            . . . . 1 . . . 
                            . . . . 1 . . . 
                            . . . . 1 . . . 
                            . . . . 1 . . . 
                            . . . . 1 . . . 
                            . . . . 1 . . .
            """),
            SpriteKindLegacy.AlienShot)
        alienShot.set_position(firingAlien.x, firingAlien.y)
        alienShot.set_velocity(0, shotSpeed)
        alienShot.set_flag(SpriteFlag.AUTO_DESTROY, True)
def initPlayer():
    global maxShots, playerSpawnDelay, extraLifeScore, nextLifeScore
    info.set_score(0)
    info.set_life(3)
    maxShots = 1
    # Time in milliseconds after player is destroyed before it will respawn.
    playerSpawnDelay = 2500
    extraLifeScore = 1500
    nextLifeScore = extraLifeScore
    resetPlayer()
def startNewLevel():
    global currLevel, spaceshipChance, alienShotChance, currAlienPause, noUpdates
    currLevel += 1
    if spaceshipChance < maxSpaceshipChance:
        spaceshipChance += spaceshipChance
        if spaceshipChance > maxSpaceshipChance:
            spaceshipChance = maxSpaceshipChance
    if alienShotChance < maxAlienShotChance:
        alienShotChance += 1
    currAlienPause = initAlienPause - alienPauseDelta * currLevel
    if currAlienPause < minAlienPause:
        currAlienPause = minAlienPause
    initScreen()
    resetAliens()
    resetPlayer()
    noUpdates = 0

def on_overlap_projectile_enemy(sprite6, otherSprite6):
    global destroyedAlien
    sprite6.destroy()
    destroyedAlien = otherSprite6
    destroyAlien()
sprites.on_overlap(SpriteKindLegacy.Projectile,
    SpriteKindLegacy.Enemy,
    on_overlap_projectile_enemy)

def on_overlap_enemy_fortress(sprite7, otherSprite7):
    otherSprite7.destroy(effects.spray, 500)
sprites.on_overlap(SpriteKindLegacy.Enemy,
    SpriteKindLegacy.Fortress,
    on_overlap_enemy_fortress)

def createSplashBase():
    global splashBase, text_list, currFont, headlinesY
    splashBase = image.create(scene.screen_width(), scene.screen_height())
    splashBase.fill(15)
    text_list = ["SPACE", "INVADERS!"]
    currFont = drawStrings.create_font_info(FontName.FONT8, 2)
    drawStrings.write_multiple_center(text_list, splashBase, 2, 5, currFont)
    headlinesY = len(text_list) * drawStrings.height(currFont) + 4
    currFont = drawStrings.create_font_info(FontName.FONT8)
    drawStrings.write_center("Press any button to start",
        splashBase,
        scene.screen_height() - (drawStrings.height(currFont) + 2),
        1,
        currFont)
    text_list = ["= " + str(alienType1Score) + " points",
        "= " + str(alienType2Score) + " points",
        "= " + str(alienType3Score) + " points",
        "= ? Mystery"]
    drawStrings.write_multiple(text_list,
        splashBase,
        scene.screen_width() / 2,
        scene.screen_height() / 2 + 0,
        1,
        currFont,
        2)
def showSplashScreen():
    global splashScreensBuilt, currSplashScreen, splashRotateInterval, nextSplashRotate
    splashScreensBuilt = 0
    createSplashBase()
    buildSplashScreens()
    currSplashScreen = 0
    splashRotateInterval = 5000
    nextSplashRotate = game.runtime() + splashRotateInterval
    scene.set_background_image(splashScreens[0])
    addGhostEnemies()
    splashScreensBuilt = 1
def addGhostEnemies():
    global attractSprite, currX, currY
    attractSprite = sprites.create(img("""
            . . . 1 1 . . . 
                    . 1 1 1 1 1 1 . 
                    1 1 1 1 1 1 1 1 
                    1 f f 1 1 f f 1 
                    1 1 1 1 1 1 1 1 
                    . . 1 . . 1 . . 
                    . 1 . . . . 1 . 
                    1 . . 1 1 . . 1
        """),
        SpriteKindLegacy.Enemy)
    currX = scene.screen_width() / 2 - 10
    currY = scene.screen_height() / 2 + 4
    attractSprite.set_position(currX, currY)
    attractSprite.set_flag(SpriteFlag.GHOST, True)
    attractSprite = sprites.create(img("""
            . 1 . . . . 1 . 
                    . . 1 . . 1 . . 
                    1 . 1 1 1 1 . 1 
                    1 1 f 1 1 f 1 1 
                    1 1 1 1 1 1 1 1 
                    . 1 1 1 1 1 1 . 
                    . . 1 . . 1 . . 
                    . 1 . . . . 1 .
        """),
        SpriteKindLegacy.Enemy)
    currY += 10
    attractSprite.set_position(currX, currY)
    attractSprite.set_flag(SpriteFlag.GHOST, True)
    attractSprite = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 1 . . 
                    . 1 1 1 1 1 1 . 
                    1 1 1 1 1 1 1 1 
                    1 1 f 1 1 f 1 1 
                    . . 1 . . 1 . . 
                    . 1 . 1 1 . 1 . 
                    1 . 1 . . 1 . 1
        """),
        SpriteKindLegacy.Enemy)
    currY += 10
    attractSprite.set_position(currX, currY)
    attractSprite.set_flag(SpriteFlag.GHOST, True)
    attractSprite = sprites.create(img("""
            . . . . . 2 2 2 2 2 2 . . . . . 
                    . . . 2 2 2 2 2 2 2 2 2 2 . . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
                    . 2 2 f 2 f 2 f f 2 f 2 f 2 2 . 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    . 2 2 2 . . 2 2 2 2 . . 2 2 2 . 
                    . . 2 . . . . . . . . . . 2 . . 
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
        SpriteKindLegacy.Enemy)
    currY += 16
    attractSprite.set_position(currX, currY)
    attractSprite.set_flag(SpriteFlag.GHOST, True)
def resetAliens():
    global heartbeatNote, tempAlienShotChance, alienShotChance, aliensMoveLeft, alien, alienX, alienY, numAliensNextSpeedup
    heartbeatNote = 0
    music.set_tempo(initHeartbeatTempo)
    tempAlienShotChance = alienShotChance
    # Do not allow aliens to shoot until all have been drawn.
    alienShotChance = 0
    aliensMoveLeft = 1
    row = 0
    while row <= numRows - 1:
        col = 0
        while col <= numCols - 1:
            alien = sprites.create(img("""
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
                """),
                SpriteKindLegacy.Enemy)
            if row == 0:
                alien.set_image(img("""
                    . . . 1 1 . . . 
                                        . . 1 1 1 1 . . 
                                        . 1 1 1 1 1 1 . 
                                        1 1 1 1 1 1 1 1 
                                        1 1 f 1 1 f 1 1 
                                        . . 1 . . 1 . . 
                                        . 1 . 1 1 . 1 . 
                                        1 . 1 . . 1 . 1
                """))
            elif row == 1:
                alien.set_image(img("""
                    . 1 . . . . 1 . 
                                        . . 1 . . 1 . . 
                                        1 . 1 1 1 1 . 1 
                                        1 1 f . . f 1 1 
                                        1 1 1 1 1 1 1 1 
                                        . 1 1 1 1 1 1 . 
                                        . . 1 . . 1 . . 
                                        . 1 . . . . 1 .
                """))
            else:
                alien.set_image(img("""
                    . . . 1 1 . . . 
                                        . 1 1 1 1 1 1 . 
                                        1 1 1 1 1 1 1 1 
                                        1 f f 1 1 f f 1 
                                        1 1 1 1 1 1 1 1 
                                        . . 1 . . 1 . . 
                                        . 1 . . . . 1 . 
                                        1 . . 1 1 . . 1
                """))
            alienX = col * (alien.width + spacing) + spacing + leftMargin
            alienY = row * (alien.height + spacing) + topMargin
            alien.set_position(alienX, alienY)
            col += 1
        row += 1
    calcNextAlienMove()
    numAliensNextSpeedup = numAliensStart / 2
    # Allow aliens to shoot.
    alienShotChance = tempAlienShotChance
def moveAliens():
    global sprite_list, aliensMoveDown, aliensMoveLeft, alienDelta, heartbeatNote
    sprite_list = sprites.all_of_kind(SpriteKindLegacy.Enemy)
    aliensMoveDown = 0
    # Should only need to look through the first row's worth of aliens to find left or right limit.
    index = 0
    while index <= numCols:
        # Ensure we're within the bounds of the list.
        if index < len(sprite_list):
            if aliensMoveLeft == 1 and sprite_list[index].x <= aliensShiftAmt:
                aliensMoveDown = 1
            elif aliensMoveLeft == 0 and sprite_list[index].x >= scene.screen_width() - aliensShiftAmt:
                aliensMoveDown = 1
        index += 1
    if aliensMoveDown == 1:
        # Change direction.
        aliensMoveLeft = 1 - aliensMoveLeft
        moveAliensDown()
    else:
        if aliensMoveLeft == 1:
            alienDelta = 0 - aliensShiftAmt
        else:
            alienDelta = aliensShiftAmt
        moveAliensHoriz()
    music.play_tone(heartbeatNotes[heartbeatNote],
        music.beat(BeatFraction.QUARTER))
    heartbeatNote += 1
    if heartbeatNote >= len(heartbeatNotes):
        heartbeatNote = 0
def playerShoot():
    global projectile
    if len(sprites.all_of_kind(SpriteKindLegacy.Projectile)) < maxShots:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . 1 . . . . 
                            . . . 1 . . . . 
                            . . . 1 . . . . 
                            . . . 1 . . . . 
                            . . . 1 . . . . 
                            . . . 1 . . . . 
                            . . 1 1 1 . . . 
                            . 1 . 1 . 1 . .
            """),
            player2,
            0,
            0 - shotSpeed)
        projectile.set_position(player2.x, player2.y)
def startAttractMode():
    global noUpdates, attractMode
    noUpdates = 1
    attractMode = 1
    showSplashScreen()
def initScreen():
    global fortressPositions, fortress
    createStarfield()
    fortressPositions = [1, 2, 4, 5, 7, 8]
    for value4 in fortressPositions:
        for index2 in range(2):
            fortress = sprites.create(img("""
                    c 6 6 6 6 6 c 6 6 6 6 6 c . . . 
                                    6 c 6 6 6 6 6 c 6 6 6 6 6 c . . 
                                    6 6 c 6 6 6 6 6 c 6 6 6 6 6 c . 
                                    6 6 6 c c c c c c c c c c c c c 
                                    6 6 6 c 7 7 7 7 7 c 7 7 7 7 7 c 
                                    6 6 6 c 7 7 7 7 7 c 7 7 7 7 7 c 
                                    c 6 6 c 7 7 7 7 7 c 7 7 7 7 7 c 
                                    6 c 6 c 7 7 7 7 7 c 7 7 7 7 7 c 
                                    6 6 c c 7 7 7 7 7 c 7 7 7 7 7 c 
                                    6 6 6 c c c c c c c c c c c c c 
                                    6 6 6 c 7 7 7 7 7 c 7 7 7 7 7 c 
                                    6 6 6 c 7 7 7 7 7 c 7 7 7 7 7 c 
                                    c 6 6 c 7 7 7 7 7 c 7 7 7 7 7 c 
                                    . c 6 c 7 7 7 7 7 c 7 7 7 7 7 c 
                                    . . c c 7 7 7 7 7 c 7 7 7 7 7 c 
                                    . . . c c c c c c c c c c c c c
                """),
                SpriteKindLegacy.Fortress)
            fortress.set_position(value4 * 16 + 8, 82 + index2 * 16)
def testForNewLevel():
    global numEnemies, noUpdates
    numEnemies = len(sprites.all_of_kind(SpriteKindLegacy.Enemy))
    numEnemies += len(sprites.all_of_kind(SpriteKindLegacy.Spaceship))
    if numEnemies == 0:
        noUpdates = 1
        music.power_up.play()
        game.splash("Level " + str((currLevel + 1)) + " cleared!")
        startNewLevel()
def moveAliensHoriz():
    for value5 in sprites.all_of_kind(SpriteKindLegacy.Enemy):
        value5.x += alienDelta
def initSpaceship():
    global spaceshipScoreIncrement, spaceshipMaxIncrements, initSpaceshipChance, maxSpaceshipChance, spaceshipChance, spaceshipSpeed
    spaceshipScoreIncrement = 50
    spaceshipMaxIncrements = 6
    initSpaceshipChance = 1
    maxSpaceshipChance = 25
    spaceshipChance = initSpaceshipChance / 2
    spaceshipSpeed = 25
def changeScore():
    global nextLifeScore
    info.change_score_by(scoreDelta)
    if info.score() >= nextLifeScore:
        nextLifeScore += extraLifeScore
        info.change_life_by(1)
        music.magic_wand.play()
def calcNextAlienMove():
    global nextAlienMove
    nextAlienMove = game.runtime() + currAlienPause
def initAliens():
    global numRows, numCols, numAliensStart, spacing, topMargin, leftMargin, aliensShiftAmt, initAlienPause, alienPauseDelta, minAlienPause, shotSpeed, currAlienPause, initAlienShotChance, maxAlienShotChance, alienShotChance, currLevel, heartbeatNotes, initHeartbeatTempo
    numRows = 4
    numCols = 9
    numAliensStart = numRows * numCols
    spacing = 4
    topMargin = 20
    leftMargin = (scene.screen_width() - (8 * numCols + spacing * (numCols + 1))) / 2 + 4
    # Number of pixels to move aliens each time.
    aliensShiftAmt = 4
    # Initial amount of time in milliseconds to pause before alien movement.
    initAlienPause = 2000
    # Amount to decrease alien pause at the start of each level.
    alienPauseDelta = 200
    minAlienPause = 500
    shotSpeed = 100
    currAlienPause = initAlienPause
    initAlienShotChance = 1
    maxAlienShotChance = 10
    alienShotChance = initAlienShotChance
    currLevel = 0
    heartbeatNotes = [196, 175, 165, 147]
    initHeartbeatTempo = 60
    resetAliens()
def buildSplashScreens():
    global splashScreens, headlines, currFont, splashScreen
    splashScreens = []
    headlines = [["Space Invaders", "is (C) 1978 Taito"],
        ["Programmed in", "MakeCode Arcade"],
        ["by", "Alex K."]]
    currFont = drawStrings.create_font_info(FontName.FONT5)
    for value6 in headlines:
        splashScreen = splashBase.clone()
        drawStrings.write_multiple_center(value6, splashScreen, headlinesY, 14, currFont)
        splashScreens.append(splashScreen)
def destroyPlayer():
    global playerRespawnTime, playerDestroyed
    player2.destroy(effects.spray, 500)
    playerRespawnTime = game.runtime() + playerSpawnDelay
    playerDestroyed = 1
    info.change_life_by(-1)
    if info.life() > 0:
        music.power_down.play()
def resetPlayer():
    global player2, playerDestroyed
    for value7 in sprites.all_of_kind(SpriteKindLegacy.Player):
        value7.destroy()
    player2 = sprites.create(img("""
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
                    . . . . . . . 7 7 . . . . . . . 
                    . . . . . 7 7 7 7 7 7 . . . . . 
                    . . . . . 7 7 7 7 7 7 . . . . . 
                    . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
        """),
        SpriteKindLegacy.Player)
    player2.set_position(scene.screen_width() / 2,
        scene.screen_height() - player2.height / 2)
    player2.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    controller.move_sprite(player2, 50, 0)
    playerDestroyed = 0
def rotateSplashScreen():
    global currSplashScreen, nextSplashRotate
    if splashScreensBuilt == 1:
        currSplashScreen += 1
        if currSplashScreen >= len(splashScreens):
            currSplashScreen = 0
        nextSplashRotate = game.runtime() + splashRotateInterval
        scene.set_background_image(splashScreens[currSplashScreen])
def createStarfield():
    global numStars, background
    numStars = 80
    background = image.create(scene.screen_width(), scene.screen_height())
    background.fill(15)
    row2 = 0
    while row2 <= numStars - 1:
        background.set_pixel(randint(0, scene.screen_width()),
            randint(0, scene.screen_height()),
            randint(3, 14))
        row2 += 1
    scene.set_background_image(background)

def on_overlap_alien_shot_fortress(sprite8, otherSprite8):
    global struckFortress
    sprite8.destroy()
    struckFortress = otherSprite8
    degradeFortress()
sprites.on_overlap(SpriteKindLegacy.AlienShot,
    SpriteKindLegacy.Fortress,
    on_overlap_alien_shot_fortress)

background: Image = None
numStars = 0
playerRespawnTime = 0
splashScreen: Image = None
headlines: List[List[str]] = []
initAlienShotChance = 0
nextAlienMove = 0
initSpaceshipChance = 0
numEnemies = 0
fortress: Sprite = None
fortressPositions: List[number] = []
player2: Sprite = None
projectile: Sprite = None
heartbeatNotes: List[number] = []
alienDelta = 0
aliensMoveDown = 0
numAliensStart = 0
topMargin = 0
alienY = 0
leftMargin = 0
spacing = 0
alienX = 0
alien: Sprite = None
numCols = 0
numRows = 0
aliensMoveLeft = 0
tempAlienShotChance = 0
initHeartbeatTempo = 0
heartbeatNote = 0
currY = 0
currX = 0
attractSprite: Sprite = None
splashScreens: List[Image] = []
nextSplashRotate = 0
splashRotateInterval = 0
currSplashScreen = 0
splashScreensBuilt = 0
headlinesY = 0
currFont: FontInfo = None
text_list: List[str] = []
splashBase: Image = None
minAlienPause = 0
alienPauseDelta = 0
initAlienPause = 0
maxAlienShotChance = 0
alienShotChance = 0
maxSpaceshipChance = 0
spaceshipChance = 0
currLevel = 0
nextLifeScore = 0
extraLifeScore = 0
playerSpawnDelay = 0
maxShots = 0
shotSpeed = 0
alienShot: Sprite = None
firingAlien: Sprite = None
sprite_list: List[Sprite] = []
playerDestroyed = 0
noUpdates = 0
currAlienPause = 0
numAliensNextSpeedup = 0
numAliensCurr = 0
spaceshipMaxIncrements = 0
spaceshipScoreIncrement = 0
scoreDelta = 0
alienImage: Image = None
attractMode = 0
fortressImage: Image = None
struckFortress: Sprite = None
destroyedAlien: Sprite = None
spaceshipSpeed = 0
spaceship: Sprite = None
aliensShiftAmt = 0
alienType3Score = 0
alienType2Score = 0
alienType1Score = 0
alienType1Score = 10
alienType2Score = 20
alienType3Score = 30
startAttractMode()

def on_on_update():
    if noUpdates == 0:
        if playerDestroyed == 1 and game.runtime() >= playerRespawnTime:
            resetPlayer()
        if game.runtime() >= nextAlienMove:
            calcNextAlienMove()
            moveAliens()
        if Math.percent_chance(alienShotChance):
            alienShoot()
        if len(sprites.all_of_kind(SpriteKindLegacy.Spaceship)) == 0 and Math.percent_chance(spaceshipChance):
            spawnSpaceship()
        testForNewLevel()
    elif attractMode == 1 and game.runtime() >= nextSplashRotate:
        rotateSplashScreen()
game.on_update(on_on_update)
