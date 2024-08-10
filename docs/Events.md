# Events
## AcceptedFactionInvite
(Multiplayer) (Client) AcceptedFactionInvite: Fires when receiving confirmation that a local player has accepted a faction invite.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| faction | string | Name of the faction. |
| username | string | Username of the faction leader. |
## AcceptedSafehouseInvite
(Multiplayer) (Client) AcceptedSafehouseInvite: Fires when a player accepts an invite to a safehouse.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| safehouse | string | Name of the safehouse. |
| username | string | Username of the safehouse owner. |
## AcceptedTrade
(Multiplayer) (Client) AcceptedTrade: Fires when the other player in the client's current trade accepts or declines the trade.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| accepted | boolean | Whether the trade was accepted. |
## AddXP
(Client) AddXP: Fires after a local character gains perk XP, except when the XP source specifically requested not to.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character who gained the XP. |
| perk | <br>[PerkFactory.Perk](https://projectzomboid.com/modding/zombie/characters/skills/PerkFactory.Perk.html) | The perk XP was gained in. |
| amount | number | The amount of XP gained. This is the final value after all modifiers. |
## DoSpecialTooltip
DoSpecialTooltip: Fires when updating the tooltip of an IsoObject with a special tooltip. Used for hover-over information about plants.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| tooltip | <br>[ObjectTooltip](https://projectzomboid.com/modding/zombie/ui/ObjectTooltip/ObjectTooltip.html) | Empty tooltip for the object. |
| square | <br>[IsoGridSquare](https://projectzomboid.com/modding/zombie/iso/IsoGridSquare.html) | Square of the object the tooltip is being updated for. |
## EveryDays
EveryDays: Fires at 0:00 every in-game day.

**Parameters**

None.
## EveryHours
EveryHours: Fires at the start of every in-game hour.

**Parameters**

None.
## EveryOneMinute
EveryOneMinute: Fires every in-game minute.

**Parameters**

None.
## EveryTenMinutes
EveryTenMinutes: Fires every ten in-game minutes.

**Parameters**

None.
## LevelPerk
(Client) LevelPerk: Fires after a local character gains or loses a perk level.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character whose perk level changed. |
| perk | <br>[PerkFactory.Perk](https://projectzomboid.com/modding/zombie/characters/skills/PerkFactory.Perk.html) | The perk that changed level. |
| level | integer | The new level of the perk. |
| increased | boolean | True if the level increased, false if it decreased. |
## LoadGridsquare
LoadGridsquare: Fires after a new square is loaded.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| square | <br>[IsoGridSquare](https://projectzomboid.com/modding/zombie/iso/IsoGridSquare.html) | The square that was loaded. |
## MngInvReceiveItems
(Multiplayer) (Client) MngInvReceiveItems: Fires when managing a remote player's inventory from the admin menu.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| inventory | MngInvItemTable | Details of the player's inventory. |
## OnAIStateChange
(Client) OnAIStateChange: Fires when a local zombie or any loaded player changes state.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character whose state changed. |
| currentState | <br>[State](https://projectzomboid.com/modding/zombie/ai/State.html) | The state the character changed to. |
| previousState | <br>[State](https://projectzomboid.com/modding/zombie/ai/State.html) | The character's previous state. |
## OnAcceptInvite
(Client) OnAcceptInvite: Fires when the client accepts a steam invite to a server.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| connectString | string | Steamworks connection string. Takes the format of '+connect ip:port' |
## onAddForageDefs
onAddForageDefs: Fires after the foraging item definitions are created.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| forageSystem | forageSystem | The foraging system. |
## OnAddMessage
(Multiplayer) (Client) OnAddMessage: Fires when a message is added to chat.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| message | <br>[ChatMessage](https://projectzomboid.com/modding/zombie/chat/ChatMessage.html) | The message that was added. |
| tabId | number | The ID of the tab the message was added to. |
## OnAdminMessage
(Multiplayer) (Client) OnAdminMessage: Fires when a ticket is created and the local player is an admin.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| message | string | The text of the ticket. |
| x | integer | World X co-ordinate of the player who made the ticket. |
| y | integer | World Y co-ordinate of the player who made the ticket. |
| z | integer | World Z co-ordinate of the player who made the ticket. |
## OnAmbientSound
OnAmbientSound: Fires whenever a sound meta event or building alarm is triggered.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| x | number | World X co-ordinate of the sound. |
| y | number | World Y co-ordinate of the sound. |
| z | number | World Z co-ordinate of the sound. |
## OnCGlobalObjectSystemInit
(Client) OnCGlobalObjectSystemInit: Fires when the client GlobalObject system is being initialised.

**Parameters**

None.
## OnChallengeQuery
(Client) OnChallengeQuery: Fires when the main menu wants to check for challenge maps.

**Parameters**

None.
## OnCharacterCollide
OnCharacterCollide: Fires when a non-zombie character collides into another (possibly zombie) character.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character colliding into the other character. |
| collidedCharacter | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character being collided into. |
## OnCharacterDeath
OnCharacterDeath: Fires when any character dies, including zombies and players regardless of whether they are local.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character who died. |
## OnChatWindowInit
(Multiplayer) (Client) OnChatWindowInit: Fires when the chat window is initialised.

**Parameters**

None.
## OnClientCommand
(Server) OnClientCommand: Fires when a client command sent through sendClientCommand is received by the server.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| module | string | The module the command was sent with. |
| command | string | The command the command was sent with. |
| player | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The player who sent the command. |
| args | table? | The arguments table the command was sent with. If the table was empty, nil is passed instead. |
## OnClimateManagerInit
OnClimateManagerInit: Fires when the climate manager is initialised.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| climateManager | <br>[ClimateManager](https://projectzomboid.com/modding/zombie/iso/weather/ClimateManager.html) | The climate manager. |
## OnClimateTick
OnClimateTick: Fires every climate manager tick.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| climateManager | <br>[ClimateManager](https://projectzomboid.com/modding/zombie/iso/weather/ClimateManager.html) | The climate manager. |
## OnClimateTickDebug
(Client) OnClimateTickDebug: Fires every climate manager tick, but only on the client and only when debug mode is enabled.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| climateManager | <br>[ClimateManager](https://projectzomboid.com/modding/zombie/iso/weather/ClimateManager.html) | The climate manager. |
## OnClothingUpdated
(Client) OnClothingUpdated: Fires every time a character's clothing is updated. This includes changing clothes and accumulating dirt or blood.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character whose clothing updated. |
## OnConnectFailed
(Multiplayer) (Client) OnConnectFailed: Fires when the client fails to connect to a server.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| message | string |  |
## OnConnected
(Multiplayer) (Client) OnConnected: Fires after successfully connecting to a server on the main menu, before character creation begins.

**Parameters**

None.
## OnConnectionStateChanged
(Multiplayer) (Client) OnConnectionStateChanged: Fires when the client's connection state is updated while trying to connect to a server.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| state | string |  |
| message | string |  |
| place | integer? |  |
## OnContainerUpdate
(Client) OnContainerUpdate: Fires when a container is added or removed from the world.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| object | any | The container that was added or removed. |
## OnCoopJoinFailed
(Client) OnCoopJoinFailed: Fires when a splitscreen character fails to be added.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| playerNum | integer | The index of the player who could not be added. |
## OnCoopServerMessage
(Multiplayer) (Server) OnCoopServerMessage: Fires when receiving a server message during a co-op (in-game hosted) game.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| tag | string |  |
| cookie | string |  |
| payload | string |  |
## OnCreateLivingCharacter
(Client) OnCreateLivingCharacter: Fires when an IsoPlayer or IsoSurvivor object is created.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoLivingCharacter](https://projectzomboid.com/modding/zombie/characters/IsoLivingCharacter.html) | The character who was created. |
| desc | <br>[SurvivorDesc](https://projectzomboid.com/modding/zombie/characters/SurvivorDesc.html) | The character's descriptor. |
## OnCreatePlayer
(Client) OnCreatePlayer: Fires every time a local player loads into the world.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| playerNum | integer | The player number of the newly-spawned character |
| player | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The new player object |
## OnCreateSurvivor
(Client) OnCreateSurvivor: Fires when an IsoSurvivor object is created.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| survivor | <br>[IsoSurvivor](https://projectzomboid.com/modding/zombie/characters/IsoSurvivor.html) | The survior that was created. |
## OnCreateUI
(Client) OnCreateUI: Fires when the UI is initialised.

**Parameters**

None.
## OnCustomUIKey
(Client) OnCustomUIKey: Fires when a key that is not used by vanilla UI is released.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| key | integer | Key code of the key that was pressed. |
## OnCustomUIKeyReleased
(Client) OnCustomUIKeyReleased: Fires when a key that is not used by vanilla UI is released.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| key | integer | Key code of the key that was pressed. |
## OnCustomUIKeyPressed
(Client) OnCustomUIKeyPressed: Fires when a key that is not used by vanilla UI is pressed.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| key | integer | Key code of the key that was pressed. |
## OnDestroyIsoThumpable
OnDestroyIsoThumpable: Fires when an IsoThumpable object is destroyed by damage.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| object | <br>[IsoThumpable](https://projectzomboid.com/modding/zombie/iso/objects/IsoThumpable.html) | The thumpable that was destroyed. |
## OnDeviceText
(Client) OnDeviceText: Fires whenever a radio displays text.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| guid | string | GUID of the line being displayed. |
| codes | string | Codes of the line being displayed. These typically contain perk/stat changes, but can be used to associate any arbitrary data with a line. |
| x | number | World X co-ordinate where the line is being displayed. |
| y | number | World Y co-ordinate where the line is being displayed. |
| z | number | World Z co-ordinate where the line is being displayed. |
| text | string | The displayed, translated text of the line. |
| device | <br>[WaveSignalDevice](https://projectzomboid.com/modding/zombie/radio/devices/WaveSignalDevice.html) | The device playing the line. |
## OnDisconnect
(Multiplayer) (Client) OnDisconnect: Fires when the client disconnects from a server.

**Parameters**

None.
## onDisableSearchMode
(Client) onDisableSearchMode: Fires when a local player disables search mode.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The character disabling search mode. |
| isSearchMode | false | Always false. |
## OnDistributionMerge
OnDistributionMerge: Fires when the distribution tables merge.

**Parameters**

None.
## OnDoTileBuilding2
(Client) OnDoTileBuilding2: Fires when the local mouse and keyboard player moves their build cursor.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| cursor | ISMoveableCursor | The build cursor object the player is dragging. |
| bRender | boolean | Whether the preview should be rendered. |
| x | integer | World X co-ordinate of the square the build cursor is over. |
| y | integer | World Y co-ordinate of the square the build cursor is over. |
| z | integer | World Z co-ordinate of the square the build cursor is over. |
| square | <br>[IsoGridSquare](https://projectzomboid.com/modding/zombie/iso/IsoGridSquare.html)? | The square the build cursor is over. |
## OnDoTileBuilding3
(Client) OnDoTileBuilding3: Fires when a controller player moves their build cursor.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| cursor | ISMoveableCursor | The cursor object the player is dragging. |
| bRender | boolean | Whether the preview should be rendered. |
| x | integer | World X co-ordinate of the square the build cursor is over. |
| y | integer | World Y co-ordinate of the square the build cursor is over. |
| z | integer | World Z co-ordinate of the square the build cursor is over. |
| square | <br>[IsoGridSquare](https://projectzomboid.com/modding/zombie/iso/IsoGridSquare.html)? | The square the build cursor is over. |
## OnDynamicMovableRecipe
(Client) OnDynamicMovableRecipe: Fires when a local character crafts a dynamically generated Movable scrapping recipe.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| sprite | string | Sprite of the movable. |
| recipe | <br>[MovableRecipe](https://projectzomboid.com/modding/zombie/scripting/objects/MovableRecipe.html) | The movable recipe that was crafted. |
| item | <br>[Moveable](https://projectzomboid.com/modding/zombie/inventory/types/Moveable.html) | The movable item being scrapped. |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character crafting the recipe. |
## onEnableSearchMode
(Client) onEnableSearchMode: Fires when a local player enables search mode.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The character disabling search mode. |
| isSearchMode | true | Always true. |
## OnEnterVehicle
(Client) OnEnterVehicle: Fires when a character enters a vehicle.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character that entered the vehicle. |
## OnEquipPrimary
OnEquipPrimary: Fires when a character equips a new item in their primary slot.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character that equipped the item. |
| item | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html) | The item that was equipped. |
## OnEquipSecondary
OnEquipSecondary: Fires when a character equips a new item in their secondary slot.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character that equipped the item. |
| item | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html) | The item that was equipped. |
## OnExitVehicle
(Client) OnExitVehicle: Fires when a character exits a vehicle.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character that exited the vehicle. |
## OnFETick
(Client) OnFETick: Fires every tick while on the main menu.

**Parameters**

None.
## OnFillContainer
(Server) OnFillContainer: Fires whenever a container is first filled with loot, or when loot respawns. Never fires for corpses.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| roomType | string | Distribution type of the room the container is in, or the type of the vehicle. |
| containerType | string | The type of the container that was filled. |
| container | <br>[ItemContainer](https://projectzomboid.com/modding/zombie/inventory/ItemContainer.html) | The container that was filled. |
## OnFillInventoryObjectContextMenu
(Client) OnFillInventoryObjectContextMenu: Fires after the context menu for an inventory item is filled.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| playerNum | integer | The number of the player whose context menu has been filled. |
| context | ISContextMenu | The context menu that was filled. |
| items | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html)[] or <br>ContextMenuItemStack[] | The items that were selected to fill the context menu. If only full stacks are selected, a table of ContextMenuItemStacks is passed. Otherwise it is a table of InventoryItems. |
## OnFillInventoryContextMenuNoItems
(Client) OnFillInventoryContextMenuNoItems: Fires after the context menu for an empty inventory is created. This event is not properly registered so you must register it before adding your function.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| playerNum | integer | The number of the player whose context menu has been filled. |
| context | ISContextMenu | The context menu that was filled. |
| isLoot | boolean | False if the container is the player's inventory. |
## onFillSearchIconContextMenu
(Client) onFillSearchIconContextMenu: Fires when opening the context menu for a foraging item.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| context | ISContextMenu | The foraging context menu. |
| icon | ISBaseIcon | The foraging icon the context menu was created for. |
## OnFillWorldObjectContextMenu
(Client) OnFillWorldObjectContextMenu: Fires after the world context menu is filled.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| playerNum | integer | The number of the player whose context menu has been filled. |
| context | ISContextMenu | The context menu that was filled. |
| worldobjects | <br>[IsoObject](https://projectzomboid.com/modding/zombie/iso/IsoObject.html)[] | The objects that were selected. |
| test | boolean | Whether the context menu was filled to test for interactive objects on the square. If true, the context menu will not actually be displayed. |
## OnGameBoot
OnGameBoot: Fires after the game finishes starting up. Note: For clients, lua files in lua/server/ will not have loaded by the time this event is fired. This does not apply to servers.

**Parameters**

None.
## OnGameStart
(Client) OnGameStart: Fires upon finishing loading and entering the game.

**Parameters**

None.
## OnGameStateEnter
(Client) OnGameStateEnter: Fires upon entering the Terms Of Service game state.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| state | <br>[State](https://projectzomboid.com/modding/zombie/ai/State.html) |  |
## OnGameTimeLoaded
OnGameTimeLoaded: Fires after GameTime is initialised.

**Parameters**

None.
## OnGamepadConnect
(Client) OnGamepadConnect: Fires after a controller is connected.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| controllerId | integer | ID of the controller. |
## OnGamepadDisconnect
(Client) OnGamepadDisconnect: Fires after a controller is disconnected.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| controllerId | integer | ID of the controller. |
## OnGetDBSchema
(Multiplayer) (Client) OnGetDBSchema: Fires when receiving the database schema from the server.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| schema | table<string, DBSchemaEntry[]> |  |
## OnGetTableResult
(Multiplayer) (Client) OnGetTableResult: Fires when receiving a database table query result from the server.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| data | <br>[ArrayList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html)<[DBResult](https://projectzomboid.com/modding/zombie/network/DBResult.html)> |  |
| rowId | integer |  |
| tableName | string |  |
## OnGridBurnt
OnGridBurnt: Fires when a square is burned by fire.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| square | <br>[IsoGridSquare](https://projectzomboid.com/modding/zombie/iso/IsoGridSquare.html) | The square that was burned. |
## OnHitZombie
OnHitZombie: Fires whenever a zombie is hit by a character.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| zombie | <br>[IsoZombie](https://projectzomboid.com/modding/zombie/characters/IsoZombie.html) | The zombie that was hit. |
| attacker | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character that hit the zombie. |
| bodyPart | <br>[BodyPartType](https://projectzomboid.com/modding/zombie/characters/BodyDamage/BodyPartType.html) | The type of the body part that was hit. |
| weapon | <br>[HandWeapon](https://projectzomboid.com/modding/zombie/inventory/types/HandWeapon.html) | The weapon the zombie was hit with. |
## OnInitGlobalModData
OnInitGlobalModData: Fires when GlobalModData is initialised. This is the earliest event after Sandbox Options are loaded.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| newGame | boolean | True if this is the first time the save has started. |
## OnInitModdedWeatherStage
OnInitModdedWeatherStage: Fires when a modded weather period is created.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| weatherPeriod | <br>[WeatherPeriod](https://projectzomboid.com/modding/zombie/iso/weather/WeatherPeriod.html) | The weather period that was created. |
| weatherStage | <br>[WeatherPeriod.WeatherStage](https://projectzomboid.com/modding/zombie/iso/weather/WeatherPeriod.WeatherStage.html) | The weather stage that was created. |
| strength | number | TODO |
## OnInitRecordedMedia
OnInitRecordedMedia: Fires when RecordedMedia is initialised.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| recordedMedia | <br>[RecordedMedia](https://projectzomboid.com/modding/zombie/radio/media/RecordedMedia.html) | The RecordedMedia object. |
## OnInitSeasons
OnInitSeasons: Fires when the ErosionManager is created.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| season | <br>[ErosionSeason](https://projectzomboid.com/modding/zombie/erosion/season/ErosionSeason.html) |  |
## OnInitWorld
OnInitWorld: Fires after the world has initialised.

**Parameters**

None.
## onItemFall
(Client) onItemFall: Fires when a local character is forced to drop the items in their hands.

**Parameters**

None.
## OnJoypadActivate
(Client) OnJoypadActivate: Fires whenever a controller starts being used during gameplay.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| joypadId | integer | ID of the joypad. |
## OnJoypadActivateUI
(Client) OnJoypadActivateUI: Fires whenever a controller starts being used outside of gameplay, such as on the main menu.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| joypadId | integer | ID of the joypad. |
## OnJoypadBeforeDeactivate
(Client) OnJoypadBeforeDeactivate: Fires when a controller is disconnected, before disconnection is processed.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| joypadId | integer | ID of the joypad. |
## OnJoypadBeforeReactivate
(Client) OnJoypadBeforeReactivate: Fires when a controller is connected, before connection is processed.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| joypadId | integer | ID of the joypad. |
## OnJoypadDeactivate
(Client) OnJoypadDeactivate: Fires after a controller has been disconnected.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| joypadId | integer | ID of the joypad. |
## OnJoypadReactivate
(Client) OnJoypadReactivate: Fires after a controller has been connected.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| joypadId | integer | ID of the joypad. |
## OnJoypadRenderUI
(Client) OnJoypadRenderUI: Fires when rendering controller debug UI.

**Parameters**

None.
## OnKeyKeepPressed
(Client) OnKeyKeepPressed: Fires every frame while a key is held down.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| key | integer | Key code of the key that was held. |
## OnKeyPressed
(Client) OnKeyPressed: Fires when a key is released.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| key | integer | Key code of the key that was released. |
## OnKeyStartPressed
(Client) OnKeyStartPressed: Fires when a key starts being pressed.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| key | integer | Key code of the key that was pressed. |
## OnLoad
(Client) OnLoad: Fires upon finishing loading and entering the game.

**Parameters**

None.
## OnLoadedMapZones
OnLoadedMapZones: Fires after loading the map zones.

**Parameters**

None.
## OnLoadedTileDefinitions
OnLoadedTileDefinitions: Fires after loading the tile definitions.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| spriteManager | <br>[IsoSpriteManager](https://projectzomboid.com/modding/zombie/iso/sprite/IsoSpriteManager.html) | The sprite manager. |
## OnLoadMapZones
OnLoadMapZones: Fires before loading the map zones.

**Parameters**

None.
## onLoadModDataFromServer
(Multiplayer) onLoadModDataFromServer: Fires when the server sends a square's moddata to the clients, or when the client receives it.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| square | <br>[IsoGridSquare](https://projectzomboid.com/modding/zombie/iso/IsoGridSquare.html) | The square that had its moddata updated. |
## OnLoadRadioScripts
OnLoadRadioScripts: Fires after ZomboidRadio loads the radio scripts.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| scriptManager | <br>[RadioScriptManager](https://projectzomboid.com/modding/zombie/radio/scripting/RadioScriptManager.html) | The radio script manager. |
| newGame | boolean | True when a new save launches for the first time. |
## OnLoadSoundBanks
(Client) OnLoadSoundBanks: Fires after the game loads the FMOD sound banks.

**Parameters**

None.
## OnMainMenuEnter
(Client) OnMainMenuEnter: Fires upon entering the main menu.

**Parameters**

None.
## OnMechanicActionDone
OnMechanicActionDone: Fires after a character completes a mechanic action on a vehicle.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character who performed the action. |
| success | boolean | Whether the action succeeded. |
| vehicleId | integer | The ID of the vehicle that was operated on. |
| partType | string | The type of the part that was operated on. |
| itemId | number |  |
| installing | boolean |  |
## OnMiniScoreboardUpdate
(Multiplayer) (Client) OnMiniScoreboardUpdate: Fires when the admin mini-scoreboard is updated.

**Parameters**

None.
## OnModsModified
(Client) OnModsModified: Fires on the main menu when a mod's files have changed.

**Parameters**

None.
## OnMouseDown
(Client) OnMouseDown: Fires when the player left clicks, as long as the input isn't eaten by UI.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| x | number | Screen X co-ordinate of the click. |
| y | number | Screen Y co-ordinate of the click. |
## OnMouseMove
(Client) OnMouseMove: Fires every frame, unless mouse movement is eaten by something else.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| x | integer | Screen X co-ordinate of the click. |
| y | integer | Screen Y co-ordinate of the click. |
| xMultiplied | integer | Screen X co-ordinate of the click multiplied by zoom level. |
| yMultiplied | integer | Screen Y co-ordinate of the click multiplied by zoom level. |
## OnMouseUp
(Client) OnMouseUp: Fires whenever the player releases the left mouse button, unless the input is eaten by UI.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| x | number | Screen X co-ordinate of the click. |
| y | number | Screen Y co-ordinate of the click. |
## OnMultiTriggerNPCEvent
OnMultiTriggerNPCEvent: Fires when the player triggers an NPC event.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| type | string |  |
| data | table |  |
| def | <br>[BuildingDef](https://projectzomboid.com/modding/zombie/iso/BuildingDef.html) |  |
## OnNewFire
OnNewFire: Fires when a new fire is started.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| fire | <br>[IsoFire](https://projectzomboid.com/modding/zombie/iso/objects/IsoFire.html) | The fire that was created. |
## OnNewGame
(Client) OnNewGame: Fires whenever a local player character is created for the first time.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| player | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The character that was created. |
| square | <br>[IsoGridSquare](https://projectzomboid.com/modding/zombie/iso/IsoGridSquare.html) | The square the character spawned on. |
## OnObjectAboutToBeRemoved
OnObjectAboutToBeRemoved: Fires before a tile object is destroyed or picked up.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| object | <br>[IsoObject](https://projectzomboid.com/modding/zombie/iso/IsoObject.html) | The object about to be removed. |
## OnObjectAdded
OnObjectAdded: Fires when an object is added to the world. Note: usually not called on the client, but is in some cases.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| object | <br>[IsoObject](https://projectzomboid.com/modding/zombie/iso/IsoObject.html) |  |
## OnObjectCollide
OnObjectCollide: Fires when two objects collide with each other.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| object | <br>[IsoMovingObject](https://projectzomboid.com/modding/zombie/iso/IsoMovingObject.html) | The object that collided into the other object. |
| collided | <br>[IsoObject](https://projectzomboid.com/modding/zombie/iso/IsoObject.html) | The object that was collided into. |
## OnObjectLeftMouseButtonDown
(Client) OnObjectLeftMouseButtonDown: Fires when the player left clicks a world object.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| object | <br>[IsoObject](https://projectzomboid.com/modding/zombie/iso/IsoObject.html) | The object that was clicked. |
| x | number | Screen X co-ordinate of the click. |
| y | number | Screen Y co-ordinate of the click. |
## OnObjectLeftMouseButtonUp
(Client) OnObjectLeftMouseButtonUp: Fires when the player releases left click on a world object.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| object | <br>[IsoObject](https://projectzomboid.com/modding/zombie/iso/IsoObject.html) | The object that was clicked. |
| x | number | Screen X co-ordinate of the click. |
| y | number | Screen Y co-ordinate of the click. |
## OnObjectRightMouseButtonDown
(Client) OnObjectRightMouseButtonDown: Fires when the player right clicks a world object.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| object | <br>[IsoObject](https://projectzomboid.com/modding/zombie/iso/IsoObject.html) | The object that was clicked. |
| x | number | Screen X co-ordinate of the click. |
| y | number | Screen Y co-ordinate of the click. |
## OnObjectRightMouseButtonUp
(Client) OnObjectRightMouseButtonUp: Fires when the player releases right click on a world object.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| object | <br>[IsoObject](https://projectzomboid.com/modding/zombie/iso/IsoObject.html) | The object that was clicked. |
| x | number | Screen X co-ordinate of the click. |
| y | number | Screen Y co-ordinate of the click. |
## OnPlayerAttackFinished
(Client) OnPlayerAttackFinished: Fires when a local player finishes attacking.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| player | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The player who attacked. |
| weapon | <br>[HandWeapon](https://projectzomboid.com/modding/zombie/inventory/types/HandWeapon.html) | The weapon the player attacked with. |
## OnPlayerDeath
(Client) OnPlayerDeath: Fires when a local player dies.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| player | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The player who died. |
## OnPlayerGetDamage
OnPlayerGetDamage: Fires every time a local player takes damage. Bleeding bodyparts fire the event once per frame each. It also fires when zombies are hit by weapons: this is the only case in which the event fires on the server.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character who took damage. |
| damageType | "POISON" or "HUNGRY" or "SICK" or <br>"BLEEDING" or "THIRST" or "HEAVYLOAD" or <br>"INFECTION" or "LOWWEIGHT" or <br>"FALLDOWN" or "WEAPONHIT" or "CARHITDAMAGE" or <br>"CARCRASHDAMAGE" | The type of damage the character took. |
| damage | number | The damage that was taken. |
## OnPlayerMove
(Client) OnPlayerMove: Fires during each local player's update if they are walking.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) |  |
## OnPlayerUpdate
(Client) OnPlayerUpdate: Fires during each local player's update (every tick).

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| player | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The player being updated. |
## OnPostDistributionMerge
OnPostDistributionMerge: Fires after the distribution tables have been merged.

**Parameters**

None.
## OnPostFloorLayerDraw
OnPostFloorLayerDraw: Fires after a floor layer has been rendered.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| z | integer | The Z level that was rendered. |
## OnPostMapLoad
OnPostMapLoad: Fires after the map has been loaded.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| cell | <br>[IsoCell](https://projectzomboid.com/modding/zombie/iso/IsoCell.html) | The cell that was loaded. |
| x | integer |  |
| y | integer |  |
## OnPostRender
(Client) OnPostRender: Fires after every in-game rendering frame.

**Parameters**

None.
## OnPostSave
OnPostSave: Fires after saving and exiting the game.

**Parameters**

None.
## OnPostUIDraw
(Client) OnPostUIDraw: Fires after every UI render frame

**Parameters**

None.
## OnPreDistributionMerge
OnPreDistributionMerge: Fires after the distribution tables have been merged.

**Parameters**

None.
## OnPreFillInventoryObjectContextMenu
(Client) OnPreFillInventoryObjectContextMenu: Fires when the context menu for an inventory item is created, before it is filled.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| playerNum | integer | The number of the player whose context menu has been created. |
| context | ISContextMenu | The context menu that was created. |
| items | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html)[] or <br>ContextMenuItemStack[] | The items that were selected to fill the context menu. If only full stacks are selected, a table of ContextMenuItemStacks is passed. Otherwise it is a table of InventoryItems. |
## OnPreFillInventoryContextMenuNoItems
(Client) OnPreFillInventoryContextMenuNoItems: Fires when the context menu for an empty inventory is created, before it is filled.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| playerNum | integer | The number of the player whose context menu has been created. |
| context | ISContextMenu | The context menu that was created. |
| isLoot | boolean | False if the container is the player's inventory. |
## OnPreFillWorldObjectContextMenu
(Client) OnPreFillWorldObjectContextMenu: Fires after the world context menu is created, before it is filled.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| playerIndex | integer | The number of the player whose context menu has been created. |
| context | ISContextMenu | The context menu that was created. |
| worldobjects | <br>[IsoObject](https://projectzomboid.com/modding/zombie/iso/IsoObject.html)[] | The objects that were selected. |
| test | boolean | Whether the context menu was created to test for interactive objects on the square. If true, the context menu will not actually be displayed. |
## OnPreMapLoad
OnPreMapLoad: Fires before the map starts loading.

**Parameters**

None.
## OnPressRackButton
(Client) OnPressRackButton: Fires when a local player has a gun and presses the button to rack it.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| player | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The player attempting to rack. |
| weapon | <br>[HandWeapon](https://projectzomboid.com/modding/zombie/inventory/types/HandWeapon.html) | The weapon they are attempting to rack. |
## OnPressReloadButton
(Client) OnPressReloadButton: Fires when a local player has a gun and presses the button to reload it.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| player | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The player attempting to reload. |
| weapon | <br>[HandWeapon](https://projectzomboid.com/modding/zombie/inventory/types/HandWeapon.html) | The weapon they are attempting to reload. |
## OnPressWalkTo
(Client) OnPressWalkTo: Fires when the local player 1 presses their Walk To keybind.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| arg0 | 0 | Always zero. |
| arg1 | 0 | Always zero. |
| arg2 | 0 | Always zero. |
## OnPreUIDraw
(Client) OnPreUIDraw: Fires before every UI render frame

**Parameters**

None.
## OnReceiveGlobalModData
(Multiplayer) OnReceiveGlobalModData: Fires when receiving a global moddata table.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| key | string | The key of the mod data table that was requested. |
| data | table or false | The mod data table that was returned. False if there was no mod data table by that key. |
## OnReceiveItemListNet
(Multiplayer) OnReceiveItemListNet: Fires when receiving a list of items from another player.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| sender | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) |  |
| items | <br>[ArrayList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html) |  |
| receiver | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) |  |
| transferID | string |  |
| custom | string |  |
## OnReceiveUserlog
(Multiplayer) (Client) OnReceiveUserlog: Fires when receiving another client's Userlogs.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| username | string |  |
| logs | <br>[ArrayList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html) |  |
## OnRefreshInventoryWindowContainers
(Client) OnRefreshInventoryWindowContainers: Fires when the available containers in the inventory UI change.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| inventoryPage | ISInventoryPage |  |
| reason | string |  |
## OnRenderTick
OnRenderTick: Fires on every rendering tick.

**Parameters**

None.
## OnResetLua
OnResetLua: Fires after Lua has been reloaded.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| reason | string |  |
## OnResolutionChange
OnResolutionChange: Fires whenever the window resolution changes.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| oldX | integer | Previous width of the window. |
| oldY | integer | Previous height of the window. |
| newX | integer | New width of the window. |
| newY | integer | New height of the window. |
## OnRightMouseDown
(Client) OnRightMouseDown: Fires when the player right clicks, as long as the input isn't eaten by UI.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| x | number | Screen X co-ordinate of the click. |
| y | number | Screen Y co-ordinate of the click. |
## OnRightMouseUp
(Client) OnRightMouseUp: Fires whenever the player releases the right mouse button, unless the input is eaten by UI.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| x | number | Screen X co-ordinate of the click. |
| y | number | Screen Y co-ordinate of the click. |
## OnSafehousesChanged
(Multiplayer) (Client) OnSafehousesChanged: Fires every time a safehouse is added, removed or changed.

**Parameters**

None.
## OnSave
OnSave: Fires while saving the world, after characters and sandbox options have been saved, but before global mod data and the world have been saved.

**Parameters**

None.
## OnScoreboardUpdate
(Multiplayer) (Client) OnScoreboardUpdate: Fires when the client receives an update to the in-game scoreboard.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| usernames | <br>[ArrayList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html) |  |
| displayNames | <br>[ArrayList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html) |  |
| steamIDs | <br>[ArrayList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html) |  |
## OnSeeNewRoom
OnSeeNewRoom: Fires when a room becomes visible for the first time.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| room | <br>[IsoRoom](https://projectzomboid.com/modding/zombie/iso/areas/IsoRoom.html) | The room. |
## OnServerCommand
(Multiplayer) (Client) OnServerCommand: Fires when a server command sent through sendServerCommand is received by the client.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| module | string | The module the command was sent with. |
| command | string | The command the command was sent with. |
| args | table? | The arguments table the command was sent with. If the table was empty, nil is passed instead. |
## OnServerFinishSaving
(Multiplayer) (Client) OnServerFinishSaving: Fires when the server has finished saving and unpauses the game.

**Parameters**

None.
## OnServerStarted
(Multiplayer) (Server) OnServerStarted: Fires when the server has started and can now be connected to.

**Parameters**

None.
## OnServerStartSaving
(Multiplayer) (Server) OnServerStartSaving: Fires when the server has paused the game to save.

**Parameters**

None.
## OnServerStatisticReceived
(Multiplayer) (Client) OnServerStatisticReceived: Fires when the MPStatistics have been received from the server.

**Parameters**

None.
## OnServerWorkshopItems
(Multiplayer) (Client) OnServerWorkshopItems: Fires when receiving an update about the server's Steam Workshop items while connecting.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| type | string |  |
## OnSetDefaultTab
(Multiplayer) (Client) OnSetDefaultTab: Fires when the player sets their favourite chat window tab.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| title | string |  |
## OnSGlobalObjectSystemInit
(Server) OnSGlobalObjectSystemInit: Fires when the server GlobalObject system has been initialised.

**Parameters**

None.
## OnSpawnRegionsLoaded
(Client) OnSpawnRegionsLoaded: Fires when the spawn regions have been loaded.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| regions | table |  |
## OnSteamFriendStatusChanged
(Client) OnSteamFriendStatusChanged: Fires when the player has gained or lost a steam friend.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| steamID | string | Steam ID of the friend who was gained/lost. |
## OnSteamGameJoin
(Multiplayer) (Client) OnSteamGameJoin: Fires when the player joins a game through steam.

**Parameters**

None.
## OnSteamRefreshInternetServers
(Client) OnSteamRefreshInternetServers: Fires when the steam server list has been refreshed.

**Parameters**

None.
## OnSteamRulesRefreshComplete
(Client) OnSteamRulesRefreshComplete: Fires after a server's rules are retrieved.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| address | string |  |
| port | integer |  |
| rules | table | Table of information about the server TODO: investigate what this actually is, class definition? |
## OnSteamServerResponded
(Client) OnSteamServerResponded: Fires when receiving a server for the server list.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| index | integer |  |
## OnSteamServerResponded2
(Client) OnSteamServerResponded2: Fires when receiving a server for the favourite server list.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| address | string |  |
| port | integer |  |
| server | <br>[Server](https://projectzomboid.com/modding/zombie/network/Server.html) |  |
## OnSteamWorkshopItemCreated
(Client) OnSteamWorkshopItemCreated: Fires when the client successfully uploads a workshop item.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| workshopId | string |  |
| bUserNeedsToAcceptWorkshopLegalAgreement | boolean |  |
## OnSteamWorkshopItemNotCreated
(Client) OnSteamWorkshopItemNotCreated: Fires when the client fails to upload a workshop item.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| result | integer |  |
## OnSteamWorkshopItemNotUpdated
(Client) OnSteamWorkshopItemNotUpdated: Fires when the client fails to update a workshop item.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| result | integer |  |
## OnSteamWorkshopItemUpdated
(Client) OnSteamWorkshopItemUpdated: Fires when the client successfully updates a workshop item.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| bUserNeedsToAcceptWorkshopLegalAgreement | boolean |  |
## OnSwitchVehicleSeat
(Client) OnSwitchVehicleSeat: Fires when a local character moves seats in a vehicle.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character who moved seats. |
## OnTabAdded
(Multiplayer) (Client) OnTabAdded: Fires when a tab is added to the chat.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| title | string |  |
| tabID | number |  |
## OnTabRemoved
(Multiplayer) (Client) OnTabRemoved: Fires when a tab is removed from the chat.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| title | string |  |
| tabID | number |  |
## OnTemplateTextInit
OnTemplateTextInit: Fires when TemplateText is initialised.

**Parameters**

None.
## OnThrowableExplode
OnThrowableExplode: Fires when a throwable or trap explodes.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| throwable | <br>[IsoTrap](https://projectzomboid.com/modding/zombie/iso/objects/IsoTrap.html) | The explosive. |
| square | <br>[IsoGridSquare](https://projectzomboid.com/modding/zombie/iso/IsoGridSquare.html) | The square it exploded on. |
## OnThunderEvent
(Client) OnThunderEvent: Fires when a thunder event is enqueued.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| x | integer | World X co-ordinate where the thunder event will happen. |
| y | integer | World Y co-ordinate where the thunder event will happen. |
| strike | boolean | Whether the thunder event will make a striking sound. |
| light | boolean | Whether the thunder event will create light. |
| rumble | boolean | Whether the thunder event will make a rumbling sound. |
## OnTick
OnTick: Fires every game tick.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| tick | number | The number of ticks since the game started. |
## OnTickEvenPaused
OnTickEvenPaused: Fires every game tick, even if the game is paused.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| tick | number | The number of ticks since the game started. Always zero while paused. |
## OnTileRemoved
OnTileRemoved: Fires when a tile object is removed.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| object | <br>[IsoObject](https://projectzomboid.com/modding/zombie/iso/IsoObject.html) | The object being removed. |
## onToggleSearchMode
(Client) onToggleSearchMode: Fires when a local player toggles search mode.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The character toggling search mode. |
| isSearchMode | boolean | Whether search mode is now on or off. |
## OnTriggerNPCEvent
OnTriggerNPCEvent: Fires when the player triggers an NPC event.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| type | string |  |
| data | table |  |
| def | <br>[BuildingDef](https://projectzomboid.com/modding/zombie/iso/BuildingDef.html) |  |
## onUpdateIcon
(Client) onUpdateIcon: Fires when an ISForageIcon is moved or removed.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| zoneData | table |  |
| iconID | string |  |
| icon | ISForageIcon |  |
## OnUpdateModdedWeatherStage
(Server) OnUpdateModdedWeatherStage: Fires when a modded weather stage tries to be updated.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| weatherPeriod | <br>[WeatherPeriod](https://projectzomboid.com/modding/zombie/iso/weather/WeatherPeriod.html) |  |
| weatherStage | WeatherStage |  |
| strength | number |  |
## OnUseVehicle
(Client) OnUseVehicle: Fires when a local character enters or exits a vehicle.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character using the vehicle. |
| vehicle | <br>[BaseVehicle](https://projectzomboid.com/modding/zombie/vehicles/BaseVehicle.html) | The vehicle being used. |
| pressedNotTapped | boolean | True if the button was held for a short duration, false if the button was tapped. |
## OnVehicleDamageTexture
OnVehicleDamageTexture: Fires when a vehicle part has become damaged enough to gain a damage overlay.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| driver | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character driving the vehicle. |
## OnWaterAmountChange
OnWaterAmountChange: Fires when the amount of water in an object changes.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| object | <br>[IsoObject](https://projectzomboid.com/modding/zombie/iso/IsoObject.html) | The object which has gained/lost water. |
| previousAmount | integer | The amount of water the object had before the change. |
## OnWeaponHitCharacter
(Client) OnWeaponHitCharacter: Fires when a non-zombie character is hit by an attack from a local player.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| attacker | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character who attacked. |
| target | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character who was hit by the attack. |
| weapon | <br>[HandWeapon](https://projectzomboid.com/modding/zombie/inventory/types/HandWeapon.html) | The weapon that was attacked with. |
| damage | number | How much damage the attack did. TODO: what does this actually mean? injuries? |
## OnWeaponHitThumpable
(Server) OnWeaponHitThumpable: Fires when an IsoThumpable is hit by an attack.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| attacker | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character attacking the object. |
| weapon | <br>[HandWeapon](https://projectzomboid.com/modding/zombie/inventory/types/HandWeapon.html) | The weapon the object was attacked with. |
| object | <br>[IsoThumpable](https://projectzomboid.com/modding/zombie/iso/objects/IsoThumpable.html) | The object that was attacked. |
## OnWeaponHitTree
(Client) OnWeaponHitTree: Fires when a tree is hit by an attack.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| attacker | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character hitting the tree. |
| weapon | <br>[HandWeapon](https://projectzomboid.com/modding/zombie/inventory/types/HandWeapon.html) | The weapon the tree was hit with. |
## OnWeaponHitXp
OnWeaponHitXp: Fires when XP is being granted for an attack.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| attacker | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character who attacked. |
| weapon | <br>[HandWeapon](https://projectzomboid.com/modding/zombie/inventory/types/HandWeapon.html) | The weapon the character attacked with. |
| target | <br>[IsoMovingObject](https://projectzomboid.com/modding/zombie/iso/IsoMovingObject.html) | The target of the attack. |
| damage | number | The damage of the attack. |
## OnWeaponSwing
OnWeaponSwing: Fires when a player begins swinging a weapon.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| attacker | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The character attacking. |
| weapon | <br>[HandWeapon](https://projectzomboid.com/modding/zombie/inventory/types/HandWeapon.html) | The weapon being attacked with. |
## OnWeaponSwingHitPoint
(Client) OnWeaponSwingHitPoint: Fires when a local player's attack connects.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| attacker | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The player attacking. |
| weapon | <br>[HandWeapon](https://projectzomboid.com/modding/zombie/inventory/types/HandWeapon.html) | The weapon being attacked with. |
## OnWeatherPeriodComplete
(Server) OnWeatherPeriodComplete: Fires when a weather period finishes.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| period | <br>[WeatherPeriod](https://projectzomboid.com/modding/zombie/iso/weather/WeatherPeriod.html) |  |
## OnWeatherPeriodStage
(Server) OnWeatherPeriodStage: Fires when a weather period progresses a stage.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| period | <br>[WeatherPeriod](https://projectzomboid.com/modding/zombie/iso/weather/WeatherPeriod.html) |  |
## OnWeatherPeriodStart
(Server) OnWeatherPeriodStart: Fires when a weather period begins.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| period | <br>[WeatherPeriod](https://projectzomboid.com/modding/zombie/iso/weather/WeatherPeriod.html) |  |
## OnWeatherPeriodStop
(Server) OnWeatherPeriodStop: Fires when a weather period ends early, such as by an admin command.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| period | <br>[WeatherPeriod](https://projectzomboid.com/modding/zombie/iso/weather/WeatherPeriod.html) |  |
## OnWorldSound
OnWorldSound: Fires whenever a world sound is created.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| x | integer | World X co-ordinate of the square the sound was created on. |
| y | integer | World Y co-ordinate of the square the sound was created on. |
| z | integer | World Z co-ordinate of the square the sound was created on. |
| radius | integer | Radius of the sound. |
| volume | integer | Volume of the sound. Zombies are more likely to investigate louder sounds when they have multiple choices. |
| source | <br>[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) | The source of the sound. |
## OnZombieDead
OnZombieDead: Fires when a zombie dies. The zombie's inventory is not filled with loot when this event fires, but their clothing and attached items are added. The corpse does not exist until a few seconds later.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| zombie | <br>[IsoZombie](https://projectzomboid.com/modding/zombie/characters/IsoZombie.html) | The zombie that died. |
## OnZombieUpdate
(Client) OnZombieUpdate: Fires whenever a zombie updates.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| zombie | <br>[IsoZombie](https://projectzomboid.com/modding/zombie/characters/IsoZombie.html) | The zombie being updated. |
## preAddCatDefs
preAddCatDefs: Fires before the foraging system processes item category definitions.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| system | forageSystem | The foraging system. |
## preAddForageDefs
preAddForageDefs: Fires before the foraging system processes any definitions.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| system | forageSystem | The foraging system. |
## preAddItemDefs
preAddItemDefs: Fires before the foraging system processes item definitions.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| system | forageSystem | The foraging system. |
## preAddSkillDefs
preAddSkillDefs: Fires before the foraging system processes trait and profession definitions.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| system | forageSystem | The foraging system. |
## preAddZoneDefs
preAddZoneDefs: Fires before the foraging system processes zone definitions.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| system | forageSystem | The foraging system. |
## ReceiveFactionInvite
(Multiplayer) (Client) ReceiveFactionInvite: Fires when the client receives a faction invite.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| factionName | string |  |
| hostUsername | string |  |
## ReceiveSafehouseInvite
(Multiplayer) (Client) ReceiveSafehouseInvite: Fires when the client receives a safehouse invite.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| title | string |  |
| hostUsername | string |  |
## RequestTrade
(Multiplayer) (Client) RequestTrade: Fires when the client receives a trade request.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| requester | string |  |
## ReuseGridsquare
ReuseGridsquare: Fires before a square is unloaded.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| square | <br>[IsoGridSquare](https://projectzomboid.com/modding/zombie/iso/IsoGridSquare.html) | The square being reused. |
## SendCustomModData
(Multiplayer) (Server) SendCustomModData: Fires when a client is requesting server moddata.

**Parameters**

None.
## ServerPinged
(Multiplayer) (Client) ServerPinged: Fires when receiving a ping response from the server. The 'numClients' string is suffixed with '/512'.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| clientAddress | string |  |
| numClients | string |  |
## SwitchChatStream
(Multiplayer) (Client) SwitchChatStream: Fires when the client switches chat tabs.

**Parameters**

None.
## SyncFaction
(Multiplayer) (Client) SyncFaction: Fires when the client receives changes to a faction.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| faction | string |  |
## TradingUIAddItem
(Multiplayer) (Client) TradingUIAddItem: Fires when the other player in a trade adds an item.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| player | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The player who added the item. |
| item | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html) | The item that was added. |
## TradingUIRemoveItem
(Multiplayer) (Client) TradingUIRemoveItem: Fires when the other player in a trade removes an item.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| player | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The player who removed the item. |
| index | integer | The index of the removed item. |
## TradingUIUpdateState
(Multiplayer) (Client) TradingUIUpdateState: Fires when the other player in a trade changes the state of the trade.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| player | <br>[IsoPlayer](https://projectzomboid.com/modding/zombie/characters/IsoPlayer.html) | The player changing the state. |
| state | integer | The new state. TODO: enum for this |
## ViewTickets
(Multiplayer) (Client) ViewTickets: Fires when receiving the list of tickets from the server.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| tickets | <br>[ArrayList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html) |  |

# Hook
## Attack
(Client) Attack: Called every tick while a local character is pressing their attack button and is able to attack.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| attacker | <br>[IsoLivingCharacter](https://projectzomboid.com/modding/zombie/characters/IsoLivingCharacter.html) | The character attempting to attack. |
| chargeDelta | number |  |
| weapon | <br>[HandWeapon](https://projectzomboid.com/modding/zombie/inventory/types/HandWeapon.html) |  |
## AutoDrink
(Client) AutoDrink: Called whenever a character automatically drinks while auto-drink is turned on.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character auto-drinking. |
## CalculateStats
(Client) CalculateStats: Called when a character's stats are being updated. Character health is not included.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) |  |
## WeaponHitCharacter
WeaponHitCharacter: Called when the effects of an attack are being calculated.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| attacker | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) |  |
| target | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) |  |
| weapon | <br>[HandWeapon](https://projectzomboid.com/modding/zombie/inventory/types/HandWeapon.html) |  |
| damageSplit | number |  |
## WeaponSwing
WeaponSwing: Called when a weapon is swung to find targets

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) |  |
| weapon | <br>[HandWeapon](https://projectzomboid.com/modding/zombie/inventory/types/HandWeapon.html) |  |

# Callbacks
## Item_OnCreate
Item_OnCreate: Called when the item is first created, before it is placed into its container. Generally used to initialise items.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| item | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html) | The item being created |
## Item_OnCooked
Item_OnCooked: Called when the item is cooked. Does not fire if the item has a ReplaceOnCooked as the item is destroyed. OnCooked functions *cannot* be inside tables or the game will not find them.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| item | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html) | The item being cooked |
## Item_OnEat
Item_OnEat: Called when a player eats the item. Called on the client eating the item only.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| item | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html) | The item being eaten |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character eating the item |
| amount | number | The fraction of the item that was eaten. |
## Item_AcceptItemFunction
Item_AcceptItemFunction: Called when checking if an item is allowed inside a container with this function assigned. The container's OnlyAcceptCategory will be checked first if it has one.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| container | <br>[ItemContainer](https://projectzomboid.com/modding/zombie/inventory/ItemContainer.html) | The container the item is being added to |
| item | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html) | The item being added to the container |

**Returns**

| Name | Type | Notes |
| --- | --- | --- |
| acceptItem | boolean | Whether to allow the item in the container |
## Recipe_OnCanPerform
Recipe_OnCanPerform: Called when checking if a character is able to perform the recipe.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| recipe | <br>[Recipe](https://projectzomboid.com/modding/zombie/scripting/objects/Recipe.html) | The recipe being checked |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character the recipe is being checked for |
| item | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html)? | The item the player right clicked to see this recipe. Null if it's being checked because of the crafting menu. |

**Returns**

| Name | Type | Notes |
| --- | --- | --- |
| canPerform | boolean | Whether to allow the character to craft the recipe |
## Recipe_OnTest
Recipe_OnTest: Called when checking if an item is allowed to be used in a recipe.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| item | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html) | The item being checked |
| result | <br>[Recipe.Result](https://projectzomboid.com/modding/zombie/scripting/objects/Recipe.Result.html) | The result of the recipe |

**Returns**

| Name | Type | Notes |
| --- | --- | --- |
| test | boolean | Whether to allow the item into the recipe |
## Recipe_OnCreate
Recipe_OnCreate: Called after crafting the recipe.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| sources | <br>[ArrayList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html)<[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html)> | The items used to craft the recipe |
| result | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html) | The item crafted by the recipe. Passed even if RemoveResultItem is set |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character who crafted the recipe |
| item | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html) | The item used in the crafting action. This is either the item that was right clicked to start the crafting, or the first source item if it was crafted from the recipe menu. |
| isPrimaryHandItem | boolean | True if item is equipped in the player's primary hand |
| isSecondaryHandItem | boolean | True if item is equipped in the player's secondary hand |
## Recipe_OnGiveXP
Recipe_OnGiveXP: Called after crafting the recipe.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| recipe | <br>[Recipe](https://projectzomboid.com/modding/zombie/scripting/objects/Recipe.html) | The recipe that was crafted |
| sources | <br>[ArrayList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html)<[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html)> | The items used to craft the recipe |
| result | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html) | The item crafted by the recipe. Passed even if RemoveResultItem is set |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character who crafted the recipe |
## Recipe_GetItemTypes
Recipe_GetItemTypes: Called by the recipe manager for every recipe source after the lua/server/ folder loads. The ArrayList should be filled with Item objects to include as part of the recipe source.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| outItems | <br>[ArrayList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html)<[Item](https://projectzomboid.com/modding/zombie/scripting/objects/Item.html)> | An empty ArrayList to be filled with items. |
## VehiclePart_init
VehiclePart_init: Called every time the part loads in or is reset.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| vehicle | <br>[BaseVehicle](https://projectzomboid.com/modding/zombie/vehicles/BaseVehicle.html) | The vehicle the part belongs to |
| part | <br>[VehiclePart](https://projectzomboid.com/modding/zombie/vehicles/VehiclePart.html) | The part being initialised |
## VehiclePart_create
VehiclePart_create: Called when the part is spawned for the first time.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| vehicle | <br>[BaseVehicle](https://projectzomboid.com/modding/zombie/vehicles/BaseVehicle.html) | The vehicle the part belongs to |
| part | <br>[VehiclePart](https://projectzomboid.com/modding/zombie/vehicles/VehiclePart.html) | The part being created |
## VehiclePart_checkEngine
VehiclePart_checkEngine: Called every tick while the engine is running. If any part returns false the engine will immediately shut off.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| vehicle | <br>[BaseVehicle](https://projectzomboid.com/modding/zombie/vehicles/BaseVehicle.html) | The vehicle the part belongs to |
| part | <br>[VehiclePart](https://projectzomboid.com/modding/zombie/vehicles/VehiclePart.html) | The part being checked |

**Returns**

| Name | Type | Notes |
| --- | --- | --- |
| working | boolean | Whether the engine should be working |
## VehiclePart_checkOperate
VehiclePart_checkOperate: Called every tick while a player is in the driver's seat and able to drive. If any part returns false the player will not be able to control the vehicle.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| vehicle | <br>[BaseVehicle](https://projectzomboid.com/modding/zombie/vehicles/BaseVehicle.html) | The vehicle the part belongs to |
| part | <br>[VehiclePart](https://projectzomboid.com/modding/zombie/vehicles/VehiclePart.html) | The part being checked |

**Returns**

| Name | Type | Notes |
| --- | --- | --- |
| operable | boolean | Whether the vehicle is operable |
## VehiclePart_update
VehiclePart_update: Called regularly to update the part, targeting a rate of every half an in-game minute (1.25 seconds on 1 hour days).

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| vehicle | <br>[BaseVehicle](https://projectzomboid.com/modding/zombie/vehicles/BaseVehicle.html) | The vehicle the part belongs to |
| part | <br>[VehiclePart](https://projectzomboid.com/modding/zombie/vehicles/VehiclePart.html) | The part being updated |
| deltaMinutes | number | The number of minutes since the last update |
## VehiclePart_use
VehiclePart_use: Called when a character interacts with the vehicle while in the part's area.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| vehicle | <br>[BaseVehicle](https://projectzomboid.com/modding/zombie/vehicles/BaseVehicle.html) | The vehicle the part belongs to |
| part | <br>[VehiclePart](https://projectzomboid.com/modding/zombie/vehicles/VehiclePart.html) | The part being used |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character using the part |
## VehiclePart_Install_test
VehiclePart_Install_test: Called when testing if the part can be installed.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| vehicle | <br>[BaseVehicle](https://projectzomboid.com/modding/zombie/vehicles/BaseVehicle.html) | The vehicle the part belongs to |
| part | <br>[VehiclePart](https://projectzomboid.com/modding/zombie/vehicles/VehiclePart.html) | The part being tested |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character using the part |

**Returns**

| Name | Type | Notes |
| --- | --- | --- |
| test | boolean | Whether the part can be installed |
## VehiclePart_Install_complete
VehiclePart_Install_complete: Called when the part is finished being installed.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| vehicle | <br>[BaseVehicle](https://projectzomboid.com/modding/zombie/vehicles/BaseVehicle.html) | The vehicle the part belongs to |
| part | <br>[VehiclePart](https://projectzomboid.com/modding/zombie/vehicles/VehiclePart.html) | The part that was installed |
## VehiclePart_Uninstall_test
VehiclePart_Uninstall_test: Called when testing if the part can be uninstalled.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| vehicle | <br>[BaseVehicle](https://projectzomboid.com/modding/zombie/vehicles/BaseVehicle.html) | The vehicle the part belongs to |
| part | <br>[VehiclePart](https://projectzomboid.com/modding/zombie/vehicles/VehiclePart.html) | The part being tested |
| character | <br>[IsoGameCharacter](https://projectzomboid.com/modding/zombie/characters/IsoGameCharacter.html) | The character using the part |

**Returns**

| Name | Type | Notes |
| --- | --- | --- |
| test | boolean | Whether the part can be uninstalled |
## VehiclePart_Uninstall_complete
VehiclePart_Uninstall_complete: Called when the part is finished being uninstalled.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| vehicle | <br>[BaseVehicle](https://projectzomboid.com/modding/zombie/vehicles/BaseVehicle.html) | The vehicle the part belongs to |
| part | <br>[VehiclePart](https://projectzomboid.com/modding/zombie/vehicles/VehiclePart.html) | The part that was uninstalled |
| item | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html) | The item that was removed |
## ItemContainer_Predicate
ItemContainer_Predicate: Used by the -Eval methods in ItemContainer. These methods will only consider items that this function returns true for.

**Parameters**

| Name | Type | Notes |
| --- | --- | --- |
| item | <br>[InventoryItem](https://projectzomboid.com/modding/zombie/inventory/InventoryItem.html) | The item being tested. |

**Returns**

| Name | Type | Notes |
| --- | --- | --- |
| allowItem | boolean | Whether the item is a valid match. |

