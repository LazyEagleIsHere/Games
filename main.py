controller.combos.attachCombo("Up + Left", function () {
    if (FirstPage) {
    	
    } else {
        timer.debounce("action", 1, function () {
            animation.runImageAnimation(
            mySprite,
            [],
            200,
            true
            )
        })
    }
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (FirstPage) {
    	
    } else {
        timer.debounce("action", 1, function () {
            animation.runImageAnimation(
            mySprite,
            [],
            200,
            true
            )
        })
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (FirstPage) {
    	
    } else {
        if (level == 1) {
            let list: number[] = []
            movements(list)
        } else if (level == 2) {
        	
        } else if (level == 3) {
        	
        } else if (level == 4) {
        	
        }
    }
})
controller.down.onEvent(ControllerButtonEvent.Released, function () {
    if (FirstPage) {
    	
    } else {
        animation.stopAnimation(animation.AnimationTypes.All, mySprite)
        mySprite.setImage()
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (FirstPage) {
    	
    } else {
        timer.debounce("action", 1, function () {
            animation.runImageAnimation(
            mySprite,
            [],
            200,
            true
            )
        })
    }
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    if (FirstPage) {
    	
    } else {
        animation.stopAnimation(animation.AnimationTypes.All, mySprite)
        mySprite.setImage()
    }
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    if (FirstPage) {
    	
    } else {
        animation.stopAnimation(animation.AnimationTypes.All, mySprite)
        mySprite.setImage()
    }
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (FirstPage) {
    	
    } else {
        timer.debounce("action", 1, function () {
            animation.runImageAnimation(
            mySprite,
            [],
            200,
            true
            )
        })
    }
})
controller.up.onEvent(ControllerButtonEvent.Released, function () {
    if (FirstPage) {
    	
    } else {
        animation.stopAnimation(animation.AnimationTypes.All, mySprite)
        mySprite.setImage()
    }
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    if (FirstPage) {
    	
    } else {
        timer.debounce("action", 1, function () {
            animation.runImageAnimation(
            mySprite,
            [],
            200,
            true
            )
        })
    }
})
function movements (action: any[]) {
	
}
controller.combos.attachCombo("Down + Left", function () {
    if (FirstPage) {
    	
    } else {
        timer.debounce("action", 1, function () {
            animation.runImageAnimation(
            mySprite,
            [],
            200,
            true
            )
        })
    }
})
controller.combos.attachCombo("Down + Right", function () {
    if (FirstPage) {
    	
    } else {
        timer.debounce("action", 1, function () {
            animation.runImageAnimation(
            mySprite,
            [],
            200,
            true
            )
        })
    }
})
controller.combos.attachCombo("Up + Right", function () {
    if (FirstPage) {
    	
    } else {
        timer.debounce("action", 1, function () {
            animation.runImageAnimation(
            mySprite,
            [],
            200,
            true
            )
        })
    }
})
let mySprite2: Sprite = null
let mySprite: Sprite = null
let level = 0
let myMenu2: miniMenu.MenuSprite = null
let FirstPage = false
FirstPage = true
let ForeverWalking = sprites.create(, SpriteKind.Player)
animation.runImageAnimation(
ForeverWalking,
[],
200,
true
)
ForeverWalking.setPosition(80, 60)
let myTextSprite = fancyText.create("SMS Adventure", 0, 1, fancyText.art_deco_11)
myTextSprite.setPosition(80, 10)
let myMenu = miniMenu.createMenu(
miniMenu.createMenuItem("Tutorial (Press Spacebar)"),
miniMenu.createMenuItem("Unlimited (Press Spacebar)"),
miniMenu.createMenuItem("Credits (Press Spacebar)")
)
myMenu.setDimensions(160, 50)
myMenu.setStyleProperty(miniMenu.StyleKind.Selected, miniMenu.StyleProperty.Background, images.colorBlock(15))
myMenu.setStyleProperty(miniMenu.StyleKind.Default, miniMenu.StyleProperty.Background, images.colorBlock(4))
myMenu.setStyleProperty(miniMenu.StyleKind.All, miniMenu.StyleProperty.Border, images.colorBlock(1))
myMenu.setPosition(80, 103)
scroller.setLayerImage(scroller.BackgroundLayer.Layer0, )
scroller.scrollBackgroundWithSpeed(-25, 0)
myMenu.onButtonPressed(controller.A, function (selection, selectedIndex) {
    if (selectedIndex == 0) {
        game.setDialogFrame()
        game.setDialogCursor()
        game.showLongText("Keyboard Control:\\n Up button: Go upward\\n Down button: Go downward\\n Left button: Go to left\\n Right button: Go to right\\n Spacebar: Attack\\n Button X: Remote attack", DialogLayout.Full)
        game.showLongText("Your mission is to collect all the treasure and leave as fast as you can. ", DialogLayout.Full)
    } else if (selectedIndex == 1) {
        myMenu.close()
        sprites.destroy(myTextSprite)
        sprites.destroyAllSpritesOfKind(SpriteKind.Player)
        scroller.setLayerImage(scroller.BackgroundLayer.Layer0, )
        myMenu2 = miniMenu.createMenu(
        miniMenu.createMenuItem("Easy", ),
        miniMenu.createMenuItem("Intermediate", ),
        miniMenu.createMenuItem("Hard", ),
        miniMenu.createMenuItem("Hell", ),
        miniMenu.createMenuItem("Cancel", )
        )
        myMenu2.setTitle("Levels")
        myMenu2.setDimensions(160, 126)
        myMenu2.setStyleProperty(miniMenu.StyleKind.Selected, miniMenu.StyleProperty.Background, images.colorBlock(15))
        myMenu2.setStyleProperty(miniMenu.StyleKind.Default, miniMenu.StyleProperty.Background, images.colorBlock(11))
        myMenu2.setStyleProperty(miniMenu.StyleKind.DefaultAndSelected, miniMenu.StyleProperty.Border, 1)
        myMenu2.setStyleProperty(miniMenu.StyleKind.DefaultAndSelected, miniMenu.StyleProperty.BorderColor, images.colorBlock(2))
        myMenu2.setPosition(80, 60)
        myMenu2.onButtonPressed(controller.A, function (selection, selectedIndex) {
            if (selectedIndex == 0) {
                myMenu2.close()
                FirstPage = false
                level = 1
                mySprite = sprites.create(, SpriteKind.Player)
                tiles.setCurrentTilemap(tilemap`level2`)
                tiles.placeOnRandomTile(mySprite, assets.tile`myTile`)
                tiles.coverAllTiles(assets.tile`myTile`, sprites.castle.tilePath5)
                controller.moveSprite(mySprite, 100, 100)
                scene.cameraFollowSprite(mySprite)
            } else if (selectedIndex == 1) {
                FirstPage = false
                level = 2
            } else if (selectedIndex == 2) {
                FirstPage = false
                level = 3
            } else if (selectedIndex == 3) {
                FirstPage = false
                level = 4
            } else if (selectedIndex == 4) {
                game.reset()
            }
        })
    } else if (selectedIndex == 2) {
        game.setDialogFrame()
        game.setDialogCursor()
        game.showLongText("Developed by SMS Student\\n3D Luk Yat Ming", DialogLayout.Full)
    }
})
game.onUpdateInterval(5000, function () {
    if (FirstPage) {
    	
    } else {
        mySprite2 = sprites.create(, SpriteKind.Enemy)
        tiles.placeOnRandomTile(mySprite2, sprites.builtin.forestTiles0)
        mySprite2.follow(mySprite, 80)
    }
})
