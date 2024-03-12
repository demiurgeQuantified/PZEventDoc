# Events
## AcceptedFactionInvite
(Multiplayer) (Client) AcceptedFactionInvite: Fires when receiving confirmation that a local player has accepted a faction invite.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| factionName | string |  |
| username | string |  |
## AcceptedSafehouseInvite
(Multiplayer) (Client) AcceptedSafehouseInvite: Fires when a player accepts an invite to a safehouse.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| safehouseTitle | string |  |
| username | string |  |
## AcceptedTrade
(Multiplayer) (Client) AcceptedTrade: Fires when the other player in the client's current trade accepts or declines the trade.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| accepted | boolean |  |
## AddXP
(Client) AddXP: Fires when a local character gains xp, unless it is flagged not to.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
| perk | PerkFactory.Perk |  |
| amount | float |  |
## DoSpecialTooltip
DoSpecialTooltip: Fires when updating the tooltip of an IsoObject with a special tooltip.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| tooltip | ObjectTooltip |  |
| square | IsoGridSquare |  |
## EveryDays
EveryDays: Fires at 0:00 every in-game day.
### Parameters
None.
## EveryHours
EveryHours: Fires at the start of every in-game hour.
### Parameters
None.
## EveryOneMinute
EveryOneMinute: Fires every in-game minute.
### Parameters
None.
## EveryTenMinutes
EveryTenMinutes: Fires every ten in-game minutes.
### Parameters
None.
## LevelPerk
(Client) LevelPerk: Fires after a local character gains or loses a perk level.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
| perk | PerkFactory.Perk |  |
| level | integer |  |
| increased | boolean |  |
## LoadGridsquare
LoadGridsquare: Fires after a new square is loaded.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| square | IsoGridSquare |  |
## MngInvReceiveItems
(Multiplayer) (Client) MngInvReceiveItems: Fires when managing a remote player's inventory from the admin menu.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| itemtable | table |  |
## OnAIStateChange
(Client) OnAIStateChange: Fires when a local zombie or any loaded player changes state.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
| currentState | State |  |
| previousState | State |  |
## OnAcceptInvite
(Client) OnAcceptInvite: Fires when the client accepts a steam invite to a server. See Steamworks API
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| connectString | string |  |
## onAddForageDefs
onAddForageDefs: Fires after the foraging item definitions are created.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| forageSystem | forageSystem |  |
## OnAddMessage
(Multiplayer) (Client) OnAddMessage: Fires when a message is added to chat.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| message | ChatMessage |  |
| tabId | short |  |
## OnAdminMessage
(Multiplayer) (Client) OnAdminMessage: Fires when a ticket is created and the local player is an admin. The co-ordinates are the location of the player creating the ticket.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| message | string |  |
| x | integer |  |
| y | integer |  |
| z | integer |  |
## OnAmbientSound
OnAmbientSound: Fires whenever a sound meta event or building alarm is triggered.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| x | float |  |
| y | float |  |
| z | float |  |
## OnCGlobalObjectSystemInit
(Client) OnCGlobalObjectSystemInit: Fires when the client GlobalObject system is being initialised.
### Parameters
None.
## OnChallengeQuery
(Client) OnChallengeQuery: Fires when the main menu wants to check for challenge maps.
### Parameters
None.
## OnCharacterCollide
OnCharacterCollide: Fires when a non-zombie character collides with another (possibly zombie) character.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
| collidedCharacter | IsoGameCharacter |  |
## OnCharacterDeath
OnCharacterDeath: Fires when any character dies, including zombies and players regardless of whether they are local.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
## OnChatWindowInit
(Multiplayer) (Client) OnChatWindowInit: Fires when the chat window is initialised.
### Parameters
None.
## OnClientCommand
(Server) OnClientCommand: Fires when a client command sent through sendClientCommand is received by the server.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| module | string |  |
| command | string |  |
| player | IsoPlayer |  |
| args | table |  |
## OnClimateManagerInit
OnClimateManagerInit: Fires when the climate manager is initialised.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| climateManager | ClimateManager |  |
## OnClimateTick
OnClimateTick: Fires every climate manager tick.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| climateManager | ClimateManager |  |
## OnClimateTickDebug
(Client) OnClimateTickDebug: Fires every climate manager tick, but only on the client and only when debug mode is enabled.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| climateManager | ClimateManager |  |
## OnClothingUpdated
(Client) OnClothingUpdated: Fires every time a character's clothing is updated. This includes when accumulating dirt or blood.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
## OnConnectFailed
(Multiplayer) (Client) OnConnectFailed: Fires when the client fails to connect to a server.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| message | string |  |
## OnConnected
(Multiplayer) (Client) OnConnected: Fires after successfully connecting to a server on the main menu, before character creation begins.
### Parameters
None.
## OnConnectionStateChanged
(Multiplayer) (Client) OnConnectionStateChanged: Fires when the client's connection state is updated while trying to connect to a server.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| state | string |  |
| message | string |  |
| place | integer? |  |
## OnContainerUpdate
(Client) OnContainerUpdate: Fires when a container is added or removed from the world.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| object | any |  |
## OnCoopJoinFailed
(Client) OnCoopJoinFailed: Fires when a splitscreen character fails to be added.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| playerIndex | integer |  |
## OnCoopServerMessage
(Multiplayer) (Server) OnCoopServerMessage: Fires when receiving a server message during a co-op (in-game hosted) game.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| tag | string |  |
| cookie | string |  |
| payload | string |  |
## OnCreateLivingCharacter
(Client) OnCreateLivingCharacter: Fires when an IsoPlayer or IsoSurvivor object is created.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoLivingCharacter |  |
| desc | SurvivorDesc |  |
## OnCreatePlayer
(Client) OnCreatePlayer: Fires every time a local player loads into the world.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| playerIndex | integer |  |
| player | IsoPlayer |  |
## OnCreateSurvivor
(Client) OnCreateSurvivor: Fires when an IsoSurvivor object is created.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| survivor | IsoSurvivor |  |
## OnCreateUI
(Client) OnCreateUI: Fires when the UI is initialised.
### Parameters
None.
## OnCustomUIKey
(Client) OnCustomUIKey: Fires when a key that is not used by vanilla UI is released.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| key | integer |  |
## OnCustomUIKeyReleased
(Client) OnCustomUIKeyReleased: Fires when a key that is not used by vanilla UI is released.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| key | integer |  |
## OnCustomUIKeyPressed
(Client) OnCustomUIKeyPressed: Fires when a key that is not used by vanilla UI is pressed.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| key | integer |  |
## OnDestroyIsoThumpable
OnDestroyIsoThumpable: Fires when an IsoThumpable object is destroyed by damage.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| object | IsoThumpable |  |
## OnDeviceText
(Client) OnDeviceText: Fires whenever a radio displays text.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| guid | string |  |
| codes | string |  |
| x | float |  |
| y | float |  |
| z | float |  |
| text | string |  |
| device | WaveSignalDevice |  |
## OnDisconnect
(Multiplayer) (Client) OnDisconnect: Fires when the client disconnects from a server.
### Parameters
None.
## onDisableSearchMode
(Client) onDisableSearchMode: Fires when a local player disables search mode.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoPlayer |  |
| isSearchMode | boolean |  |
## OnDistributionMerge
OnDistributionMerge: Fires when the distribution tables merge.
### Parameters
None.
## OnDoTileBuilding2
(Client) OnDoTileBuilding2: Fires when the local mouse and keyboard player builds something.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| cursor | ISMoveableCursor |  |
| bRender | boolean |  |
| x | integer |  |
| y | integer |  |
| z | integer |  |
| square | IsoGridSquare |  |
## OnDoTileBuilding3
(Client) OnDoTileBuilding3: Fires when a controller player builds something.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| cursor | ISMoveableCursor |  |
| bRender | boolean |  |
| x | integer |  |
| y | integer |  |
| z | integer |  |
| square | IsoGridSquare |  |
## OnDynamicMovableRecipe
(Client) OnDynamicMovableRecipe: Fires when a local character crafts a dynamically generated Moveable scrapping recipe.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| sprite | string |  |
| recipe | MoveableRecipe |  |
| item | Moveable |  |
| character | IsoGameCharacter |  |
## onEnableSearchMode
(Client) onEnableSearchMode: Fires when a local player enables search mode.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoPlayer |  |
| isSearchMode | boolean |  |
## OnEnterVehicle
(Client) OnEnterVehicle: Fires when a character enters a vehicle.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
## OnEquipPrimary
OnEquipPrimary: Fires when a character equips a new item in their primary slot.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
| item | InventoryItem |  |
## OnEquipSecondary
OnEquipSecondary: Fires when a character equips a new item in their secondary slot.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
| item | InventoryItem |  |
## OnExitVehicle
(Client) OnExitVehicle: Fires when a character exits a vehicle.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
## OnFETick
(Client) OnFETick: Fires every tick while on the main menu.
### Parameters
None.
## OnFillContainer
(Server) OnFillContainer: Fires whenever a container is first filled with loot, or when loot respawns. Never fires for corpses. For vehicle containers, the roomType is instead the vehicle type.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| roomType | string |  |
| containerType | string |  |
| container | ItemContainer |  |
## OnFillInventoryObjectContextMenu
(Client) OnFillInventoryObjectContextMenu: Fires after the context menu for an inventory item is created.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| playerIndex | integer |  |
| context | ISContextMenu |  |
| items | table |  |
## OnFillInventoryContextMenuNoItems
(Client) OnFillInventoryContextMenuNoItems: Fires after the context menu for an empty inventory is created.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| playerIndex | integer |  |
| context | ISContextMenu |  |
| isLoot | boolean |  |
## onFillSearchIconContextMenu
(Client) onFillSearchIconContextMenu: Fires when opening the context menu for a foraging item.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| context | ISContextMenu |  |
| icon | ISBaseIcon |  |
## OnFillWorldObjectContextMenu
(Client) OnFillWorldObjectContextMenu: Fires after the context menu for a world object is created.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| playerIndex | integer |  |
| context | ISContextMenu |  |
| worldobjects | table |  |
| test | boolean |  |
## OnGameBoot
OnGameBoot: Fires after the game finishes starting up. Note: For clients, lua files in lua/server/ will not have loaded by the time this event is fired. This does not apply to servers.
### Parameters
None.
## OnGameStart
(Client) OnGameStart: Fires upon finishing loading and entering the game.
### Parameters
None.
## OnGameStateEnter
(Client) OnGameStateEnter: Fires upon entering the Terms Of Service game state.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| state | State |  |
## OnGameTimeLoaded
OnGameTimeLoaded: Fires after GameTime is initialised.
### Parameters
None.
## OnGamepadConnect
(Client) OnGamepadConnect: Fires after a controller is connected.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| controllerId | integer |  |
## OnGamepadDisconnect
(Client) OnGamepadDisconnect: Fires after a controller is disconnected.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| controllerId | integer |  |
## OnGetDBSchema
(Multiplayer) (Client) OnGetDBSchema: Fires when receiving the database schema from the server.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| schema | table |  |
## OnGetTableResult
(Multiplayer) (Client) OnGetTableResult: Fires when receiving a database table query result from the server.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| data | ArrayList |  |
| rowId | integer |  |
| tableName | string |  |
## OnGridBurnt
OnGridBurnt: Fires when a square is burned by fire.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| square | IsoGridSquare |  |
## OnHitZombie
OnHitZombie: Fires whenever a zombie is hit by a character.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| zombie | IsoZombie |  |
| attacker | IsoGameCharacter |  |
| bodyPart | BodyPartType |  |
| weapon | HandWeapon |  |
## OnInitGlobalModData
OnInitGlobalModData: Fires when GlobalModData is initialised. This is the earliest event after Sandbox Options are loaded.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| newGame | boolean |  |
## OnInitModdedWeatherStage
OnInitModdedWeatherStage: Fires when a modded weather period is created.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| weatherPeriod | WeatherPeriod |  |
| weatherStage | WeatherStage |  |
| strength | float |  |
## OnInitRecordedMedia
OnInitRecordedMedia: Fires when RecordedMedia is initialised.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| recordedMedia | RecordedMedia |  |
## OnInitSeasons
OnInitSeasons: Fires when the ErosionManager is created.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| season | ErosionSeason |  |
## OnInitWorld
OnInitWorld: Fires after the world has initialised.
### Parameters
None.
## onItemFall
(Client) onItemFall: Fires when a local character is forced to drop the items in their hands.
### Parameters
None.
## OnJoypadActivate
(Client) OnJoypadActivate: Fires whenever a controller starts being used during gameplay.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| joypadId | integer |  |
## OnJoypadActivateUI
(Client) OnJoypadActivateUI: Fires whenever a controller starts being used outside of gameplay, such as on the main menu.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| joypadId | integer |  |
## OnJoypadBeforeDeactivate
(Client) OnJoypadBeforeDeactivate: Fires when a controller is disconnected, before disconnection is processed.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| joypadId | double |  |
## OnJoypadBeforeReactivate
(Client) OnJoypadBeforeReactivate: Fires when a controller is connected, before connection is processed.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| joypadId | double |  |
## OnJoypadDeactivate
(Client) OnJoypadDeactivate: Fires after a controller has been disconnected.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| joypadId | double |  |
## OnJoypadReactivate
(Client) OnJoypadReactivate: Fires after a controller has been connected.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| joypadId | double |  |
## OnJoypadRenderUI
(Client) OnJoypadRenderUI: Fires when rendering controller debug UI.
### Parameters
None.
## OnKeyKeepPressed
(Client) OnKeyKeepPressed: Fires every frame while a key is held down.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| key | integer |  |
## OnKeyPressed
(Client) OnKeyPressed: Fires when a key is released.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| key | integer |  |
## OnKeyStartPressed
(Client) OnKeyStartPressed: Fires when a key starts being pressed.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| key | integer |  |
## OnLoad
(Client) OnLoad: Fires upon finishing loading and entering the game.
### Parameters
None.
## OnLoadedMapZones
OnLoadedMapZones: Fires after loading the map zones.
### Parameters
None.
## OnLoadedTileDefinitions
OnLoadedTileDefinitions: Fires after loading the tile definitions.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| spriteManager | IsoSpriteManager |  |
## OnLoadMapZones
OnLoadMapZones: Fires before loading the map zones.
### Parameters
None.
## onLoadModDataFromServer
(Multiplayer) onLoadModDataFromServer: Fires when the server sends a square's moddata to the clients, or when the client receives it.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| square | IsoGridSquare |  |
## OnLoadRadioScripts
OnLoadRadioScripts: Fires after ZomboidRadio loads the radio scripts.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| scriptManager | RadioScriptManager |  |
| newGame | boolean |  |
## OnLoadSoundBanks
(Client) OnLoadSoundBanks: Fires after the game loads the FMOD sound banks.
### Parameters
None.
## OnMainMenuEnter
(Client) OnMainMenuEnter: Fires upon entering the main menu.
### Parameters
None.
## OnMechanicActionDone
OnMechanicActionDone: Fires after a character completes a mechanic action on a vehicle.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
| success | boolean |  |
| vehicleId | integer |  |
| partId | string |  |
| itemId | long |  |
| installing | boolean |  |
## OnMiniScoreboardUpdate
(Multiplayer) (Client) OnMiniScoreboardUpdate: Fires when the admin mini-scoreboard is updated.
### Parameters
None.
## OnModsModified
(Client) OnModsModified: Fires on the main menu when a mod's files have changed.
### Parameters
None.
## OnMouseDown
(Client) OnMouseDown: Fires when the player left clicks, as long as the input isn't eaten by UI.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| x | double |  |
| y | double |  |
## OnMouseMove
(Client) OnMouseMove: Fires every frame, unless mouse movement is eaten by something else. The latter two values are the first two multiplied by the mouse player's zoom level.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| x | integer |  |
| y | integer |  |
| xMultiplied | integer |  |
| yMultiplied | integer |  |
## OnMouseUp
(Client) OnMouseUp: Fires whenever the player releases the left mouse button, unless the input is eaten by UI.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| x | double |  |
| y | double |  |
## OnMultiTriggerNPCEvent
OnMultiTriggerNPCEvent: Fires when the player triggers an NPC event.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| type | string |  |
| data | table |  |
| def | BuildingDef |  |
## OnNewFire
OnNewFire: Fires when a new fire is started.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| fire | IsoFire |  |
## OnNewGame
(Client) OnNewGame: Fires whenever a local player character is created for the first time.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| player | IsoPlayer |  |
| square | IsoGridSquare |  |
## OnObjectAboutToBeRemoved
OnObjectAboutToBeRemoved: Fires before a tile object is destroyed or picked up.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| object | IsoObject |  |
## OnObjectAdded
OnObjectAdded: Fires when an object is added to the world. Note: usually not called on the client, but is in some cases.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| object | IsoObject |  |
## OnObjectCollide
OnObjectCollide: Fires when two objects collide with each other.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| object | IsoMovingObject |  |
| collided | IsoObject |  |
## OnObjectLeftMouseButtonDown
(Client) OnObjectLeftMouseButtonDown: Fires when the player left clicks a world object.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| object | IsoObject |  |
| x | double |  |
| y | double |  |
## OnObjectLeftMouseButtonUp
(Client) OnObjectLeftMouseButtonUp: Fires when the player releases left click on a world object.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| object | IsoObject |  |
| x | double |  |
| y | double |  |
## OnObjectRightMouseButtonDown
(Client) OnObjectRightMouseButtonDown: Fires when the player right clicks a world object.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| object | IsoObject |  |
| x | double |  |
| y | double |  |
## OnObjectRightMouseButtonUp
(Client) OnObjectRightMouseButtonUp: Fires when the player releases right click on a world object.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| object | IsoObject |  |
| x | double |  |
| y | double |  |
## OnPlayerAttackFinished
(Client) OnPlayerAttackFinished: Fires when a local player finishes attacking.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| player | IsoPlayer |  |
| weapon | HandWeapon |  |
## OnPlayerDeath
(Client) OnPlayerDeath: Fires when a local player dies.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| player | IsoPlayer |  |
## OnPlayerGetDamage
OnPlayerGetDamage: Fires every time a local player takes damage. Bleeding bodyparts fire the event once per frame each. Possible damageTypes are: POISON, HUNGRY, SICK, BLEEDING, THIRST, HEAVYLOAD, INFECTION, LOWWEIGHT, FALLDOWN, FIRE, WEAPONHIT, CARHITDAMAGE, CARCRASHDAMAGE It also fires when zombies are hit by weapons: this is the only case in which the event fires on the server.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
| damageType | string |  |
| damage | float |  |
## OnPlayerMove
(Client) OnPlayerMove: Fires during each local player's update if they are walking.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoPlayer |  |
## OnPlayerUpdate
(Client) OnPlayerUpdate: Fires during each local player's update (every tick).
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| player | IsoPlayer |  |
## OnPostDistributionMerge
OnPostDistributionMerge: Fires after the distribution tables have been merged.
### Parameters
None.
## OnPostFloorLayerDraw
OnPostFloorLayerDraw: Fires after a floor layer has been rendered.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| z | integer |  |
## OnPostMapLoad
OnPostMapLoad: Fires after the map has been loaded.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| cell | IsoCell |  |
| x | integer |  |
| y | integer |  |
## OnPostRender
(Client) OnPostRender: Fires after every in-game rendering frame.
### Parameters
None.
## OnPostSave
OnPostSave: Fires after saving and exiting the game.
### Parameters
None.
## OnPostUIDraw
(Client) OnPostUIDraw: Fires after every UI render frame
### Parameters
None.
## OnPreDistributionMerge
OnPreDistributionMerge: Fires after the distribution tables have been merged.
### Parameters
None.
## OnPreFillInventoryObjectContextMenu
(Client) OnPreFillInventoryObjectContextMenu: Fires while the context menu for an inventory item is being created, before vanilla options are added.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| playerIndex | integer |  |
| context | ISContextMenu |  |
| items | table |  |
## OnPreFillInventoryContextMenuNoItems
(Client) OnPreFillInventoryContextMenuNoItems: Fires while the context menu for an empty inventory is being created, before vanilla options are added.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| playerIndex | integer |  |
| context | ISContextMenu |  |
| isLoot | boolean |  |
## OnPreFillWorldObjectContextMenu
(Client) OnPreFillWorldObjectContextMenu: Fires while the context menu for a world object is being created, before vanilla options are added.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| playerIndex | integer |  |
| context | ISContextMenu |  |
| worldobjects | table |  |
| test | boolean |  |
## OnPreMapLoad
OnPreMapLoad: Fires before the map starts loading.
### Parameters
None.
## OnPressRackButton
(Client) OnPressRackButton: Fires when a local player has a gun and presses the button to rack it.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| player | IsoPlayer |  |
| weapon | HandWeapon |  |
## OnPressReloadButton
(Client) OnPressReloadButton: Fires when a local player has a gun and presses the button to reload it.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| player | IsoPlayer |  |
| weapon | HandWeapon |  |
## OnPressWalkTo
(Client) OnPressWalkTo: Fires when the local player 1 presses their Walk To keybind. The values passed are always 0,0,0 
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| arg0 | integer |  |
| arg1 | integer |  |
| arg2 | integer |  |
## OnPreUIDraw
(Client) OnPreUIDraw: Fires before every UI render frame
### Parameters
None.
## OnReceiveGlobalModData
(Multiplayer) OnReceiveGlobalModData: Fires when receiving a global moddata table. The table argument is false if the table did not exist.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| tableName | string |  |
| data | table |  |
## OnReceiveItemListNet
(Multiplayer) OnReceiveItemListNet: Fires when receiving a list of items from another player.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| sender | IsoPlayer |  |
| items | ArrayList |  |
| receiver | IsoPlayer |  |
| transferID | string |  |
| custom | string |  |
## OnReceiveUserlog
(Multiplayer) (Client) OnReceiveUserlog: Fires when receiving another client's Userlogs.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| username | string |  |
| logs | ArrayList |  |
## OnRefreshInventoryWindowContainers
(Client) OnRefreshInventoryWindowContainers: Fires when the available containers in the inventory UI change.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| inventoryPage | ISInventoryPage |  |
| reason | string |  |
## OnRenderTick
OnRenderTick: Fires on every rendering tick.
### Parameters
None.
## OnResetLua
OnResetLua: Fires after Lua has been reloaded.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| reason | string |  |
## OnResolutionChange
OnResolutionChange: Fires whenever the window resolution changes.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| oldX | integer |  |
| oldY | integer |  |
| newX | integer |  |
| newY | integer |  |
## OnRightMouseDown
(Client) OnRightMouseDown: Fires when the player right clicks, as long as the input isn't eaten by UI.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| x | double |  |
| y | double |  |
## OnRightMouseUp
(Client) OnRightMouseUp: Fires whenever the player releases the right mouse button, unless the input is eaten by UI.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| x | double |  |
| y | double |  |
## OnSafehousesChanged
(Multiplayer) (Client) OnSafehousesChanged: Fires every time a safehouse is added, removed or changed.
### Parameters
None.
## OnSave
OnSave: Fires while saving the world, after characters and sandbox options have been saved, but before global mod data and the world have been saved.
### Parameters
None.
## OnScoreboardUpdate
(Multiplayer) (Client) OnScoreboardUpdate: Fires when the client receives an update to the in-game scoreboard.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| usernames | ArrayList |  |
| displayNames | ArrayList |  |
| steamIDs | ArrayList |  |
## OnSeeNewRoom
OnSeeNewRoom: Fires when a room becomes visible for the first time.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| room | IsoRoom |  |
## OnServerCommand
(Multiplayer) (Client) OnServerCommand: Fires when a server command sent through sendServerCommand is received by the client.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| module | string |  |
| command | string |  |
| args | table |  |
## OnServerFinishSaving
(Multiplayer) (Client) OnServerFinishSaving: Fires when the server has finished saving and unpauses the game.
### Parameters
None.
## OnServerStarted
(Multiplayer) (Server) OnServerStarted: Fires when the server has started and can now be connected to.
### Parameters
None.
## OnServerStartSaving
(Multiplayer) (Server) OnServerStartSaving: Fires when the server has paused the game to save.
### Parameters
None.
## OnServerStatisticReceived
(Multiplayer) (Client) OnServerStatisticReceived: Fires when the MPStatistics have been received from the server.
### Parameters
None.
## OnServerWorkshopItems
(Multiplayer) (Client) OnServerWorkshopItems: Fires when receiving an update about the server's Steam Workshop items while connecting.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| type | string |  |
## OnSetDefaultTab
(Multiplayer) (Client) OnSetDefaultTab: Fires when the player sets their favourite chat window tab.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| title | string |  |
## OnSGlobalObjectSystemInit
(Server) OnSGlobalObjectSystemInit: Fires when the server GlobalObject system has been initialised.
### Parameters
None.
## OnSpawnRegionsLoaded
(Client) OnSpawnRegionsLoaded: Fires when the spawn regions have been loaded.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| regions | table |  |
## OnSteamFriendStatusChanged
(Client) OnSteamFriendStatusChanged: Fires when the player has gained or lost a steam friend.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| steamID | string |  |
## OnSteamGameJoin
(Multiplayer) (Client) OnSteamGameJoin: Fires when the player joins a game through steam.
### Parameters
None.
## OnSteamRefreshInternetServers
(Client) OnSteamRefreshInternetServers: Fires when the steam server list has been refreshed.
### Parameters
None.
## OnSteamRulesRefreshComplete
(Client) OnSteamRulesRefreshComplete: Fires after a server's rules are retrieved. 'rules' is a table of information about the server.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| address | string |  |
| port | integer |  |
| rules | table |  |
## OnSteamServerResponded
(Client) OnSteamServerResponded: Fires when receiving a server for the server list.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| index | integer |  |
## OnSteamServerResponded2
(Client) OnSteamServerResponded2: Fires when receiving a server for the favourited server list.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| address | string |  |
| port | integer |  |
| server | Server |  |
## OnSteamWorkshopItemCreated
(Client) OnSteamWorkshopItemCreated: Fires when the client successfully uploads a workshop item.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| workshopId | string |  |
| bUserNeedsToAcceptWorkshopLegalAgreement | boolean |  |
## OnSteamWorkshopItemNotCreated
(Client) OnSteamWorkshopItemNotCreated: Fires when the client fails to upload a workshop item.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| result | integer |  |
## OnSteamWorkshopItemNotUpdated
(Client) OnSteamWorkshopItemNotUpdated: Fires when the client fails to update a workshop item.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| result | integer |  |
## OnSteamWorkshopItemUpdated
(Client) OnSteamWorkshopItemUpdated: Fires when the client successfully updates a workshop item.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| bUserNeedsToAcceptWorkshopLegalAgreement | boolean |  |
## OnSwitchVehicleSeat
(Client) OnSwitchVehicleSeat: Fires when a local character moves seats in a vehicle.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
## OnTabAdded
(Multiplayer) (Client) OnTabAdded: Fires when a tab is added to the chat.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| title | string |  |
| tabID | short |  |
## OnTabRemoved
(Multiplayer) (Client) OnTabRemoved: Fires when a tab is removed from the chat.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| title | string |  |
| tabID | short |  |
## OnTemplateTextInit
OnTemplateTextInit: Fires when TemplateText is initialised.
### Parameters
None.
## OnThrowableExplode
OnThrowableExplode: Fires when a throwable or trap explodes.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| throwable | IsoTrap |  |
| square | IsoGridSquare |  |
## OnThunderEvent
(Client) OnThunderEvent: Fires when thunder hits.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| x | integer |  |
| y | integer |  |
| strike | boolean |  |
| light | boolean |  |
| rumble | boolean |  |
## OnTick
OnTick: Fires every game tick.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| tick | double |  |
## OnTickEvenPaused
OnTickEvenPaused: Fires every game tick, even if the game is paused. Tick is 0 while paused.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| tick | double |  |
## OnTileRemoved
OnTileRemoved: Fires when a tile object is removed.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| object | IsoObject |  |
## onToggleSearchMode
(Client) onToggleSearchMode: Fires when a local player toggles search mode.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoPlayer |  |
| isSearchMode | boolean |  |
## OnTriggerNPCEvent
OnTriggerNPCEvent: Fires when the player triggers an NPC event.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| type | string |  |
| data | table |  |
| def | BuildingDef |  |
## onUpdateIcon
(Client) onUpdateIcon: Fires when an ISForageIcon is moved or removed.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| zoneData | table |  |
| iconID | string |  |
| icon | ISForageIcon |  |
## OnUpdateModdedWeatherStage
(Server) OnUpdateModdedWeatherStage: Fires when a modded weather stage tries to be updated.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| weatherPeriod | WeatherPeriod |  |
| weatherStage | WeatherStage |  |
| strength | float |  |
## OnUseVehicle
(Client) OnUseVehicle: Fires when a local character enters or exits a vehicle.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
| vehicle | BaseVehicle |  |
| pressedNotTapped | boolean |  |
## OnVehicleDamageTexture
OnVehicleDamageTexture: Fires when a vehicle part has become damaged enough to gain a damage overlay.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| driver | IsoGameCharacter |  |
## OnWaterAmountChange
OnWaterAmountChange: Fires when the amount of water in an object changes.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| object | IsoObject |  |
| previousAmount | integer |  |
## OnWeaponHitCharacter
(Client) OnWeaponHitCharacter: Fires when a non-zombie character is hit by an attack.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| attacker | IsoGameCharacter |  |
| target | IsoGameCharacter |  |
| weapon | HandWeapon |  |
| damage | float |  |
## OnWeaponHitThumpable
(Server) OnWeaponHitThumpable: Fires when an IsoThumpable is hit by an attack.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| attacker | IsoGameCharacter |  |
| weapon | HandWeapon |  |
| object | IsoThumpable |  |
## OnWeaponHitTree
(Client) OnWeaponHitTree: Fires when a tree is hit by an attack.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| attacker | IsoGameCharacter |  |
| weapon | HandWeapon |  |
## OnWeaponHitXp
OnWeaponHitXp: Fires when XP is being granted for an attack.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| attacker | IsoGameCharacter |  |
| weapon | HandWeapon |  |
| target | IsoMovingObject |  |
| damage | float |  |
## OnWeaponSwing
OnWeaponSwing: Fires when a player begins swinging a weapon.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| attacker | IsoPlayer |  |
| weapon | HandWeapon |  |
## OnWeaponSwingHitPoint
(Client) OnWeaponSwingHitPoint: Fires when a local player's attack connects.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| attacker | IsoPlayer |  |
| weapon | HandWeapon |  |
## OnWeatherPeriodComplete
(Server) OnWeatherPeriodComplete: Fires when a weather period finishes.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| period | WeatherPeriod |  |
## OnWeatherPeriodStage
(Server) OnWeatherPeriodStage: Fires when a weather period progresses a stage.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| period | WeatherPeriod |  |
## OnWeatherPeriodStart
(Server) OnWeatherPeriodStart: Fires when a weather period begins.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| period | WeatherPeriod |  |
## OnWeatherPeriodStop
(Server) OnWeatherPeriodStop: Fires when a weather period ends early, such as by an admin command.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| period | WeatherPeriod |  |
## OnWorldSound
OnWorldSound: Fires whenever a world sound is created.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| x | integer |  |
| y | integer |  |
| z | integer |  |
| radius | integer |  |
| volume | integer |  |
| source | Object |  |
## OnZombieDead
OnZombieDead: Fires when a zombie dies. The zombie's inventory is not filled with loot when this event fires, but their clothing and attached items are added.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| zombie | IsoZombie |  |
## OnZombieUpdate
(Client) OnZombieUpdate: Fires whenever a zombie updates.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| zombie | IsoZombie |  |
## preAddCatDefs
preAddCatDefs: Fires before the foraging system processes item category definitions.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| system | forageSystem |  |
## preAddForageDefs
preAddForageDefs: Fires before the foraging system processes any definitions.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| system | forageSystem |  |
## preAddItemDefs
preAddItemDefs: Fires before the foraging system processes item definitions.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| system | forageSystem |  |
## preAddSkillDefs
preAddSkillDefs: Fires before the foraging system processes trait and profession definitions.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| system | forageSystem |  |
## preAddZoneDefs
preAddZoneDefs: Fires before the foraging system processes zone definitions.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| system | forageSystem |  |
## ReceiveFactionInvite
(Multiplayer) (Client) ReceiveFactionInvite: Fires when the client receives a faction invite.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| factionName | string |  |
| hostUsername | string |  |
## ReceiveSafehouseInvite
(Multiplayer) (Client) ReceiveSafehouseInvite: Fires when the client receives a safehouse invite.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| title | string |  |
| hostUsername | string |  |
## RequestTrade
(Multiplayer) (Client) RequestTrade: Fires when the client receives a trade request.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| requester | string |  |
## ReuseGridsquare
ReuseGridsquare: Fires before a square is unloaded.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| square | IsoGridSquare |  |
## SendCustomModData
(Multiplayer) (Server) SendCustomModData: Fires when a client is requesting server moddata.
### Parameters
None.
## ServerPinged
(Multiplayer) (Client) ServerPinged: Fires when receiving a ping response from the server. The 'numClients' string is suffixed with '/512'.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| clientAddress | string |  |
| numClients | string |  |
## SwitchChatStream
(Multiplayer) (Client) SwitchChatStream: Fires when the client switches chat tabs.
### Parameters
None.
## SyncFaction
(Multiplayer) (Client) SyncFaction: Fires when the client receives changes to a faction.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| faction | string |  |
## TradingUIAddItem
(Multiplayer) (Client) TradingUIAddItem: Fires when the other player in a trade adds an item.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| player | IsoPlayer |  |
| item | InventoryItem |  |
## TradingUIRemoveItem
(Multiplayer) (Client) TradingUIRemoveItem: Fires when the other player in a trade removes an item.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| player | IsoPlayer |  |
| index | integer |  |
## TradingUIUpdateState
(Multiplayer) (Client) TradingUIUpdateState: Fires when the other player in a trade changes the state of the trade.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| player | IsoPlayer |  |
| state | integer |  |
## ViewTickets
(Multiplayer) (Client) ViewTickets: Fires when receiving the list of tickets from the server.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| tickets | ArrayList |  |

# Hook
## Attack
(Client) Attack: Called every tick while a local character is pressing their attack button and is able to attack.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| attacker | IsoLivingCharacter |  |
| chargeDelta | float |  |
| weapon | HandWeapon |  |
## AutoDrink
(Client) AutoDrink: Called whenever a character automatically drinks while auto-drink is turned on.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
## CalculateStats
(Client) CalculateStats: Called when a character's stats are being updated. Character health is not included.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
## WeaponHitCharacter
WeaponHitCharacter: Called when the effects of an attack are being calculated.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| attacker | IsoGameCharacter |  |
| target | IsoGameCharacter |  |
| weapon | HandWeapon |  |
| damageSplit | float |  |
## WeaponSwing
WeaponSwing: Called when a weapon is swung to find targets
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| character | IsoGameCharacter |  |
| weapon | HandWeapon |  |

# Callbacks
## Item_OnCreate
Item_OnCreate: Called when the item is first created, before it is placed into its container. Generally used to initialise items.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| item | InventoryItem | The item being created |
## Item_OnCooked
Item_OnCooked: Called when the item is cooked. Does not fire if the item has a ReplaceOnCooked as the item is destroyed. OnCooked functions *cannot* be inside tables or the game will not find them.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| item | InventoryItem | The item being cooked |
## Item_OnEat
Item_OnEat: Called when a player eats the item. Called on the client eating the item only.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| item | InventoryItem | The item being eaten |
| character | IsoGameCharacter | The character eating the item |
| amount | float | The fraction of the item that was eaten. |
## Item_AcceptItemFunction
Item_AcceptItemFunction: Called when checking if an item is allowed inside a container with this function assigned. The container's OnlyAcceptCategory will be checked first if it has one.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| container | ItemContainer | The container the item is being added to |
| item | InventoryItem | The item being added to the container |
### Returns
| Name | Type | Notes |
| --- | --- | --- |
| acceptItem | boolean | Whether to allow the item in the container |
## Recipe_OnCanPerform
Recipe_OnCanPerform: Called when checking if a character is able to perform the recipe.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| recipe | Recipe | The recipe being checked |
| character | IsoGameCharacter | The character the recipe is being checked for |
| item | InventoryItem? | The item the player right clicked to see this recipe. Null if it's being checked because of the crafting menu. |
### Returns
| Name | Type | Notes |
| --- | --- | --- |
| canPerform | boolean | Whether to allow the character to craft the recipe |
## Recipe_OnTest
Recipe_OnTest: Called when checking if an item is allowed to be used in a recipe.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| item | InventoryItem | The item being checked |
| result | Result | The result of the recipe |
### Returns
| Name | Type | Notes |
| --- | --- | --- |
| test | boolean | Whether to allow the item into the recipe |
## Recipe_OnCreate
Recipe_OnCreate: Called after crafting the recipe.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| sources | ArrayList<InventoryItem> | The items used to craft the recipe |
| result | InventoryItem | The item crafted by the recipe. Passed even if RemoveResultItem is set |
| character | IsoGameCharacter | The character who crafted the recipe |
| item | InventoryItem | The item used in the crafting action. This is either the item that was right clicked to start the crafting, or the first source item if it was crafted from the recipe menu. |
| isPrimaryHandItem | boolean | True if item is equipped in the player's primary hand |
| isSecondaryHandItem | boolean | True if item is equipped in the player's secondary hand |
## Recipe_OnGiveXP
Recipe_OnGiveXP: Called after crafting the recipe.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| recipe | Recipe | The recipe that was crafted |
| sources | ArrayList<InventoryItem> | The items used to craft the recipe |
| result | InventoryItem | The item crafted by the recipe. Passed even if RemoveResultItem is set |
| character | IsoGameCharacter | The character who crafted the recipe |
## VehiclePart_init
VehiclePart_init: Called every time the part loads in or is reset.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| vehicle | BaseVehicle | The vehicle the part belongs to |
| part | VehiclePart | The part being initialised |
## VehiclePart_create
VehiclePart_create: Called when the part is spawned for the first time.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| vehicle | BaseVehicle | The vehicle the part belongs to |
| part | VehiclePart | The part being created |
## VehiclePart_checkEngine
VehiclePart_checkEngine: Called every tick while the engine is running. If any part returns false the engine will immediately shut off.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| vehicle | BaseVehicle | The vehicle the part belongs to |
| part | VehiclePart | The part being checked |
### Returns
| Name | Type | Notes |
| --- | --- | --- |
| working | boolean | Whether the engine should be working |
## VehiclePart_checkOperate
VehiclePart_checkOperate: Called every tick while a player is in the driver's seat and able to drive. If any part returns false the player will not be able to control the vehicle.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| vehicle | BaseVehicle | The vehicle the part belongs to |
| part | VehiclePart | The part being checked |
### Returns
| Name | Type | Notes |
| --- | --- | --- |
| operable | boolean | Whether the vehicle is operable |
## VehiclePart_update
VehiclePart_update: Called regularly to update the part, targeting a rate of every half an in-game minute (1.25 seconds on 1 hour days).
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| vehicle | BaseVehicle | The vehicle the part belongs to |
| part | VehiclePart | The part being updated |
| deltaMinutes | float | The number of minutes since the last update |
## VehiclePart_use
VehiclePart_use: Called when a character interacts with the vehicle while in the part's area.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| vehicle | BaseVehicle | The vehicle the part belongs to |
| part | VehiclePart | The part being used |
| character | IsoGameCharacter | The character using the part |
## VehiclePart_Install_test
VehiclePart_Install_test: Called when testing if the part can be installed.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| vehicle | BaseVehicle | The vehicle the part belongs to |
| part | VehiclePart | The part being tested |
| character | IsoGameCharacter | The character using the part |
### Returns
| Name | Type | Notes |
| --- | --- | --- |
| test | boolean | Whether the part can be installed |
## VehiclePart_Install_complete
VehiclePart_Install_complete: Called when the part is finished being installed.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| vehicle | BaseVehicle | The vehicle the part belongs to |
| part | VehiclePart | The part that was installed |
## VehiclePart_Uninstall_test
VehiclePart_Uninstall_test: Called when testing if the part can be uninstalled.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| vehicle | BaseVehicle | The vehicle the part belongs to |
| part | VehiclePart | The part being tested |
| character | IsoGameCharacter | The character using the part |
### Returns
| Name | Type | Notes |
| --- | --- | --- |
| test | boolean | Whether the part can be uninstalled |
## VehiclePart_Uninstall_complete
VehiclePart_Uninstall_complete: Called when the part is finished being uninstalled.
### Parameters
| Name | Type | Notes |
| --- | --- | --- |
| vehicle | BaseVehicle | The vehicle the part belongs to |
| part | VehiclePart | The part that was uninstalled |
| item | InventoryItem | The item that was removed |

