namespace SpriteKind {
    export const NPC = SpriteKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    game.setDialogTextColor(15)
    game.setDialogFrame()
    game.showLongText("what", DialogLayout.Bottom)
})
scene.setBackgroundImage()
