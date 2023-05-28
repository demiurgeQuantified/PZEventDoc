# Events
Event | Description | Parameters
--- | --- | ---
AcceptedFactionInvite | (Multiplayer) (Client) Fires when a player accepts an invite to a faction. | String factionName, String username, 
AcceptedSafehouseInvite | (Multiplayer) (Client) Fires when a player accepts an invite to a safehouse. | String safehouseTitle, String username, 
AcceptedTrade | (Multiplayer) (Client) Fires when the other player in the client's current trade accepts or declines the trade. | boolean accepted, 
AddXP | (Client) Fires when a local character gains xp, unless it is flagged not to. | IsoGameCharacter character, PerkFactory.Perk perk, float amount, 
DoSpecialTooltip | Fires when updating the tooltip of an IsoObject with a special tooltip. | ObjectTooltip tooltip, IsoGridSquare square, 
EveryDays | Fires at 0:00 every in-game day. | 
EveryHours | Fires at the start of every in-game hour. | 
EveryOneMinute | Fires every in-game minute. | 
EveryTenMinutes | Fires every ten in-game minutes. | 
LevelPerk | (Client) Fires after a local character gains or loses a perk level. | IsoGameCharacter character, PerkFactory.Perk perk, int level, boolean increased, 
LoadGridsquare | Fires after a new square is loaded. | IsoGridSquare square, 
MngInvReceiveItems | (Multiplayer) (Client) Fires when managing a remote player's inventory from the admin menu. | table itemtable, 
OnAIStateChange | (Client) Fires when a local character (zombie, player) changes state. | IsoGameCharacter character, State currentState, State previousState, 
OnAIStateEnter | (Deprecated)  | 
OnAIStateExecute | (Deprecated)  | 
OnAIStateExit | (Deprecated)  | 
OnAcceptInvite | (Client) Fires when the client accepts a steam invite to a server. See Steamworks API | String connectString, 
OnAddBuilding | (Deprecated)  | 
onAddForageDefs | Fires after the foraging item definitions are created. | table forageSystem, 
OnAddMessage | (Multiplayer) (Client) Fires when a message is added to chat. | ChatMessage message, short tabId, 
OnAdminMessage | (Multiplayer) (Client) Fires when a ticket is created and the local player is an admin. The co-ordinates are the location of the player creating the ticket. | String message, int x, int y, int z, 
OnAmbientSound | Fires whenever a sound meta event or building alarm is triggered. | float x, float y, float z, 
OnBeingHitByZombie | (Deprecated)  | 
OnCGlobalObjectSystemInit | (Client) Fires when the client GlobalObject system is being initialised. | 
OnChallengeQuery | (Client) Fires when the main menu wants to check for challenge maps. | 
OnChangeWeather | (Deprecated)  | 
OnCharacterCollide | Fires when a non-zombie character collides with another (possibly zombie) character. | IsoGameCharacter character, IsoGameCharacter collidedCharacter, 
OnCharacterCreateStats | (Deprecated)  | 
OnCharacterDeath | Fires when a character dies. | IsoGameCharacter character, 
OnCharacterMeet | (Deprecated)  | 
OnChatWindowInit | (Multiplayer) (Client) Fires when the chat window is initialised. | 
OnClientCommand | (Server) Fires when a client command sent through sendClientCommand is received by the server. | String module, String command, IsoPlayer player, table args, 
OnClimateManagerInit | Fires when the climate manager is initialised. | ClimateManager climateManager, 
OnClimateTick | Fires every climate manager tick. | ClimateManager climateManager, 
OnClimateTickDebug | (Client) Fires every climate manager tick, but only on the client and only when debug mode is enabled. | ClimateManager climateManager, 
OnClothingUpdated | (Client) Fires every time a character's clothing is updated. This includes when accumulating dirt or blood. | IsoGameCharacter character, 
OnConnectFailed | (Multiplayer) (Client) Fires when the client fails to connect to a server. | String message, 
OnConnected | (Multiplayer) (Client) Fires while connecting to a server. | 
OnConnectionStateChanged | (Multiplayer) (Client) Fires when the client's connection state is updated while trying to connect to a server. | 1: String state, String message, 2: String state, String message, int place, 
OnContainerUpdate | (Client) Fires when a container is added or removed from the world. | any object, 
OnCoopJoinFailed | (Client) Fires when a splitscreen character fails to be added. | int playerIndex, 
OnCoopServerMessage | (Multiplayer) (Server) Fires when receiving a server message during a co-op (in-game hosted) game. | String tag, String cookie, String payload, 
OnCreateLivingCharacter | (Client) Fires when an IsoPlayer or IsoSurvivor object is created. | IsoLivingCharacter character, SurvivorDesc desc, 
OnCreatePlayer | (Client) Fires every time a local player loads into the world. | int playerIndex, IsoPlayer player, 
OnCreateSurvivor | (Client) Fires when an IsoSurvivor object is created. | IsoSurvivor survivor, 
OnCreateUI | (Client) Fires when the UI is initialised. | 
OnCustomUIKey | (Client) Fires when a key that is not used by vanilla UI is released. | int key, 
OnCustomUIKeyReleased | (Client) Fires when a key that is not used by vanilla UI is released. | int key, 
OnCustomUIKeyPressed | (Client) Fires when a key that is not used by vanilla UI is pressed. | int key, 
OnDawn | (Deprecated)  | 
OnDestroyIsoThumpable | Fires when an IsoThumpable object is destroyed by damage. | IsoThumpable object, 
OnDeviceText | (Client) Fires whenever a radio displays text. | String guid, String codes, float x, float y, float z, String text, WaveSignalDevice device, 
OnDisconnect | (Multiplayer) (Client) Fires when the client disconnects from a server. | 
onDisableSearchMode | (Client) Fires when a local player disables search mode. | IsoPlayer character, boolean isSearchMode, 
OnDistributionMerge | Fires when the distribution tables merge. | 
OnDoTileBuilding | (Deprecated)  | 
OnDoTileBuilding2 | (Client) Fires when the local mouse and keyboard player builds something. | table cursor, boolean bRender, int x, int y, int z, IsoGridSquare square, 
OnDoTileBuilding3 | (Client) Fires when a controller player builds something. | table cursor, boolean bRender, int x, int y, int z, IsoGridSquare square, 
OnDusk | (Deprecated)  | 
OnDynamicMovableRecipe | (Client) Fires when a local character crafts a dynamically generated Moveable scrapping recipe. | String sprite, MoveableRecipe recipe, Moveable item, IsoGameCharacter character, 
onEnableSearchMode | (Client) Fires when a local player enables search mode. | IsoPlayer character, boolean isSearchMode, 
OnEnterVehicle | (Client) Fires when a character enters a vehicle. | IsoGameCharacter character, 
OnEquipPrimary | Fires when a character equips a new item in their primary slot. | IsoGameCharacter character, InventoryItem item, 
OnEquipSecondary | Fires when a character equips a new item in their secondary slot. | IsoGameCharacter character, InventoryItem item, 
OnExitVehicle | (Client) Fires when a character exits a vehicle. | IsoGameCharacter character, 
OnFETick | (Client) Fires every tick while on the main menu. | 
OnFillContainer | (Server) Fires whenever a container is first filled with loot, or when loot respawns. Never fires for corpses. For vehicle containers, the roomType is instead the vehicle type. | String roomType, String containerType, ItemContainer container, 
OnFillInventoryObjectContextMenu | (Client) Fires after the context menu for an inventory item is created. | int playerIndex, table context, table items, 
OnFillInventoryContextMenuNoItems | (Client) Fires after the context menu for an empty inventory is created. | int playerIndex, table context, boolean isLoot, 
onFillSearchIconContextMenu | (Client) Fires when opening the context menu for a foraging item. | table context, table icon, 
OnFillWorldObjectContextMenu | (Client) Fires after the context menu for a world object is created. | int playerIndex, table context, table worldobjects, boolean test, 
OnGameBoot | Fires after the game finishes starting up. Note: For clients, lua files in lua/server/ will not have loaded by the time this event is fired. This does not apply to servers. | 
OnGameStart | Fires upon finishing loading and entering the game. | 
OnGameStateEnter | (Client) Fires upon entering the Terms Of Service game state. | State state, 
OnGameTimeLoaded | Fires after GameTime is initialised. | 
OnGamepadConnect | (Client) Fires after a controller is connected. | int controllerId, 
OnGamepadDisconnect | (Client) Fires after a controller is disconnected. | int controllerId, 
OnGetDBSchema | (Multiplayer) (Client) Fires when receiving the database schema from the server. | table schema, 
OnGetTableResult | (Multiplayer) (Client) Fires when receiving a database table query result from the server. | ArrayList data, int rowId, String tableName, 
OnGridBurnt | Fires when a square is burned by fire. | IsoGridSquare square, 
OnHitZombie | Fires whenever a zombie is hit by a character. | IsoZombie zombie, IsoGameCharacter attacker, BodyPartType bodyPart, HandWeapon weapon, 
OnInitGlobalModData | Fires when GlobalModData is initialised. This is the earliest event after Sandbox Options are loaded. | boolean newGame, 
OnInitModdedWeatherStage | Fires when a modded weather period is created. | WeatherPeriod weatherPeriod, WeatherStage weatherStage, float strength, 
OnInitRecordedMedia | Fires when RecordedMedia is initialised. | RecordedMedia recordedMedia, 
OnInitSeasons | Fires when the ErosionManager is created. | ErosionSeason season, 
OnInitWorld | Fires after the world has initialised. | 
OnIsoThumpableLoad | (Deprecated)  | 
OnIsoThumpableSave | (Deprecated)  | 
onItemFall | (Client) Fires when a local character is forced to drop the items in their hands. | 
OnJoypadActivate | (Client) Fires whenever a controller starts being used during gameplay. | int joypadId, 
OnJoypadActivateUI | (Client) Fires whenever a controller starts being used outside of gameplay, such as on the main menu. | int joypadId, 
OnJoypadBeforeDeactivate | (Client) Fires when a controller is disconnected, before disconnection is processed. | double joypadId, 
OnJoypadBeforeReactivate | (Client) Fires when a controller is connected, before connection is processed. | double joypadId, 
OnJoypadDeactivate | (Client) Fires after a controller has been disconnected. | double joypadId, 
OnJoypadReactivate | (Client) Fires after a controller has been connected. | double joypadId, 
OnJoypadRenderUI | (Client) Fires when rendering controller debug UI. | 
OnKeyKeepPressed | (Client) Fires every frame while a key is held down. | int key, 
OnKeyPressed | (Client) Fires when a key is released. | int key, 
OnKeyStartPressed | (Client) Fires when a key starts being pressed. | int key, 
OnLoad | Fires upon finishing loading and entering the game. | 
OnLoadedMapZones | Fires after loading the map zones. | 
OnLoadedTileDefinitions | Fires after loading the tile definitions. | IsoSpriteManager spriteManager, 
OnLoadMapZones | Fires before loading the map zones. | 
onLoadModDataFromServer | (Multiplayer) Fires when the server sends a square's moddata to the clients, or when the client receives it. | IsoGridSquare square, 
OnLoadRadioScripts | Fires after ZomboidRadio loads the radio scripts. | RadioScriptManager scriptManager, boolean newGame, 
OnLoadSoundBanks | (Client) Fires after the game loads the FMOD sound banks. | 
OnLoginState | (Deprecated)  | 
OnLoginStateSuccess | (Deprecated)  | 
OnMainMenuEnter | (Client) Fires upon entering the main menu. | 
OnMakeItem | (Deprecated)  | 
OnMapLoadCreateIsoObject | (Deprecated)  | 
OnMechanicActionDone | Fires after a character completes a mechanic action on a vehicle. | IsoGameCharacter character, boolean success, int vehicleId, String partId, long itemId, boolean installing, 
OnMiniScoreboardUpdate | (Multiplayer) (Client) Fires when the admin mini-scoreboard is updated. | 
OnModsModified | (Client) Fires on the main menu when a mod's files have changed. | 
OnMouseDown | (Client) Fires when the player left clicks, as long as the input isn't eaten by UI. | double x, double y, 
OnMouseMove | (Client) Fires every frame, unless mouse movement is eaten by something else. The latter two values are the first two multiplied by the mouse player's zoom level. | int x, int y, int xMultiplied, int yMultiplied, 
OnMouseUp | (Client) Fires whenever the player releases the left mouse button, unless the input is eaten by UI. | double x, double y, 
OnMultiTriggerNPCEvent | Fires when the player triggers an NPC event. | String type, table data, BuildingDef def, 
OnNewFire | Fires when a new fire is started. | IsoFire fire, 
OnNewGame | (Client) Fires whenever a local player character is created for the first time. | IsoPlayer player, IsoGridSquare square, 
OnNewSurvivorGroup | (Deprecated)  | 
OnNPCSurvivorUpdate | (Deprecated)  | 
OnObjectAboutToBeRemoved | Fires before an object is removed from the world. | IsoObject object, 
OnObjectAdded | Fires when an object is added to the world. Note: usually not called on the client, but is in some cases. | IsoObject object, 
OnObjectCollide | Fires when two objects collide with each other. | IsoMovingObject object, IsoObject collided, 
OnObjectLeftMouseButtonDown | (Client) Fires when the player left clicks a world object. | IsoObject object, double x, double y, 
OnObjectLeftMouseButtonUp | (Client) Fires when the player releases left click on a world object. | IsoObject object, double x, double y, 
OnObjectRightMouseButtonDown | (Client) Fires when the player right clicks a world object. | IsoObject object, double x, double y, 
OnObjectRightMouseButtonUp | (Client) Fires when the player releases right click on a world object. | IsoObject object, double x, double y, 
OnPlayerAttackFinished | (Client) Fires when a local player finishes attacking. | IsoPlayer player, HandWeapon weapon, 
OnPlayerDeath | (Client) Fires when a local player dies. | IsoPlayer player, 
OnPlayerGetDamage | Fires every time a local player takes damage. Bleeding bodyparts fire the event once per frame each. Possible damageTypes are: POISON, HUNGRY, SICK, BLEEDING, THIRST, HEAVYLOAD, INFECTION, LOWWEIGHT, FALLDOWN, FIRE, WEAPONHIT, CARHITDAMAGE, CARCRASHDAMAGE It also fires when zombies are hit by weapons: this is the only case in which the event fires on the server. | IsoGameCharacter character, String damageType, float damage, 
OnPlayerMove | (Client) Fires every time a local player moves. | IsoPlayer character, 
OnPlayerSetSafehouse | (Deprecated)  | 
OnPlayerUpdate | (Client) Fires every time a local player updates. | IsoPlayer player, 
OnPostCharactersSquareDraw | (Deprecated)  | 
OnPostDistributionMerge | Fires after the distribution tables have been merged. | 
OnPostFloorLayerDraw | Fires after a floor layer has been rendered. | int z, 
OnPostFloorSquareDraw | (Deprecated)  | 
OnPostMapLoad | Fires after the map has been loaded. | IsoCell cell, int x, int y, 
OnPostRender | (Client) Fires after every in-game rendering frame. | 
OnPostSave | Fires after saving and exiting the game. | 
OnPostTileDraw | (Deprecated)  | 
OnPostTilesSquareDraw | (Deprecated)  | 
OnPostUIDraw | (Client) Fires after every UI render frame | 
OnPostWallSquareDraw | (Deprecated)  | 
OnPreDistributionMerge | Fires after the distribution tables have been merged. | 
OnPreFillInventoryObjectContextMenu | (Client) Fires while the context menu for an inventory item is being created, before vanilla options are added. | int playerIndex, table context, table items, 
OnPreFillInventoryContextMenuNoItems | (Client) Fires while the context menu for an empty inventory is being created, before vanilla options are added. | int playerIndex, table context, boolean isLoot, 
OnPreFillWorldObjectContextMenu | (Client) Fires while the context menu for a world object is being created, before vanilla options are added. | int playerIndex, table context, table worldobjects, boolean test, 
OnPreGameStart | (Deprecated)  | 
OnPreMapLoad | Fires before the map starts loading. | 
OnPressRackButton | (Client) Fires when a local player has a gun and presses the button to rack it. | IsoPlayer player, HandWeapon weapon, 
OnPressReloadButton | (Client) Fires when a local player has a gun and presses the button to reload it. | IsoPlayer player, HandWeapon weapon, 
OnPressWalkTo | (Client) Fires when the local player 1 presses their Walk To keybind. The values passed are always 0,0,0  | int arg0, int arg1, int arg2, 
OnPreUIDraw | (Client) Fires before every UI render frame | 
OnRadioInteraction | (Deprecated)  | 
OnRainStart | (Deprecated)  | 
OnRainStop | (Deprecated)  | 
OnReceiveGlobalModData | (Multiplayer) Fires when receiving a global moddata table. The table argument is false if the table did not exist. | String tableName, table table, 
OnReceiveItemListNet | (Multiplayer) Fires when receiving a list of items from another player. | IsoPlayer sender, ArrayList items, IsoPlayer receiver, String transferID, String custom, 
OnReceiveUserlog | (Multiplayer) (Client) Fires when receiving another client's Userlogs. | String username, ArrayList logs, 
OnRefreshInventoryWindowContainers | (Client) Fires when the available containers in the inventory UI change. | table inventoryPage, String reason, 
OnRenderTick | Fires on every rendering tick. | 
OnRenderUpdate | (Deprecated)  | 
OnResetLua | Fires after Lua has been reloaded. | String reason, 
OnResolutionChange | Fires whenever the window resolution changes. | int oldX, int oldY, int newX, int newY, 
OnRightMouseDown | (Client) Fires when the player right clicks, as long as the input isn't eaten by UI. | double x, double y, 
OnRightMouseUp | (Client) Fires whenever the player releases the right mouse button, unless the input is eaten by UI. | double x, double y, 
OnSafehousesChanged | (Multiplayer) (Client) Fires every time a safehouse is added, removed or changed. | 
OnSave | Fires while saving the world. | 
OnScoreboardUpdate | (Multiplayer) (Client) Fires when the client receives an update to the in-game scoreboard. | ArrayList usernames, ArrayList displayNames, ArrayList steamIDs, 
OnSeeNewRoom | Fires when a room becomes visible for the first time. | IsoRoom room, 
OnServerCommand | (Multiplayer) (Client) Fires when a server command sent through sendServerCommand is received by the client. | String module, String command, table args, 
OnServerFinishSaving | (Multiplayer) (Client) Fires when the server has finished saving and unpauses the game. | 
OnServerStarted | (Multiplayer) (Server) Fires when the server has started and can now be connected to. | 
OnServerStartSaving | (Multiplayer) (Server) Fires when the server has paused the game to save. | 
OnServerStatisticReceived | (Multiplayer) (Client) Fires when the MPStatistics have been received from the server. | 
OnServerWorkshopItems | (Multiplayer) (Client) Fires when receiving an update about the server's Steam Workshop items while connecting. | 1: String type, 2: String type, ArrayList requiredItems, 3: String type, String message, 4: String type, long ID, String Error, 5: String type, String steamID, long bytesDownloaded, long bytesRemaining, 
OnSetDefaultTab | (Multiplayer) (Client) Fires when the player sets their favourite chat window tab. | String title, 
OnSGlobalObjectSystemInit | (Server) Fires when the server GlobalObject system has been initialised. | 
OnSpawnRegionsLoaded | (Client) Fires when the spawn regions have been loaded. | table regions, 
OnSteamFriendStatusChanged | (Client) Fires when the player has gained or lost a steam friend. | String steamID, 
OnSteamGameJoin | (Multiplayer) (Client) Fires when the player joins a game through steam. | 
OnSteamRefreshInternetServers | (Client) Fires when the steam server list has been refreshed. | 
OnSteamRulesRefreshComplete | (Client) Fires after a server's rules are retrieved. 'rules' is a table of information about the server. | String address, int port, table rules, 
OnSteamServerResponded | (Client) Fires when receiving a server for the server list. | int index, 
OnSteamServerResponded2 | (Client) Fires when receiving a server for the favourited server list. | String address, int port, Server server, 
OnSteamWorkshopItemCreated | (Client) Fires when the client successfully uploads a workshop item. | String workshopId, boolean bUserNeedsToAcceptWorkshopLegalAgreement, 
OnSteamWorkshopItemNotCreated | (Client) Fires when the client fails to upload a workshop item. | int result, 
OnSteamWorkshopItemNotUpdated | (Client) Fires when the client fails to update a workshop item. | int result, 
OnSteamWorkshopItemUpdated | (Client) Fires when the client successfully updates a workshop item. | boolean bUserNeedsToAcceptWorkshopLegalAgreement, 
OnSwitchVehicleSeat | (Client) Fires when a local character moves seats in a vehicle. | IsoGameCharacter character, 
OnTabAdded | (Multiplayer) (Client) Fires when a tab is added to the chat. | String title, short tabID, 
OnTabRemoved | (Multiplayer) (Client) Fires when a tab is removed from the chat. | String title, short tabID, 
OnTemplateTextInit | Fires when TemplateText is initialised. | 
OnThrowableExplode | Fires when a throwable or trap explodes. | IsoTrap throwable, IsoGridSquare square, 
OnThunderEvent | (Client) Fires when thunder hits. | int x, int y, boolean strike, boolean light, boolean rumble, 
OnTick | Fires every game tick. | double tick, 
OnTickEvenPaused | Fires every game tick, even if the game is paused. Tick is 0 while paused. | double tick, 
OnTileRemoved | Fires when a tile object is removed. | IsoObject object, 
onToggleSearchMode | (Client) Fires when a local player toggles search mode. | IsoPlayer character, boolean isSearchMode, 
OnTriggerNPCEvent | Fires when the player triggers an NPC event. | String type, table data, BuildingDef def, 
onUpdateIcon | (Client) Fires when an ISForageIcon is moved or removed. | table zoneData, string iconID, table icon, 
OnUpdateModdedWeatherStage | (Server) Fires when a modded weather stage tries to be updated. | WeatherPeriod weatherPeriod, WeatherStage weatherStage, float strength, 
OnUseVehicle | (Client) Fires when a local character enters or exits a vehicle. | IsoGameCharacter character, BaseVehicle vehicle, boolean pressedNotTapped, 
OnVehicleDamageTexture | Fires when a vehicle part has become damaged enough to gain a damage overlay. | IsoGameCharacter driver, 
OnVehicleHorn | (Deprecated)  | 
OnWaterAmountChange | Fires when the amount of water in an object changes. | IsoObject object, int previousAmount, 
OnWeaponHitCharacter | (Client) Fires when a non-zombie character is hit by an attack. | IsoGameCharacter attacker, IsoGameCharacter target, HandWeapon weapon, float damage, 
OnWeaponHitThumpable | (Server) Fires when an IsoThumpable is hit by an attack. | IsoGameCharacter attacker, HandWeapon weapon, IsoThumpable object, 
OnWeaponHitTree | (Client) Fires when a tree is hit by an attack. | IsoGameCharacter attacker, HandWeapon weapon, 
OnWeaponHitXp | Fires when XP is being granted for an attack. | IsoGameCharacter attacker, HandWeapon weapon, IsoMovingObject target, float damage, 
OnWeaponSwing | Fires when a player begins swinging a weapon. | IsoPlayer attacker, HandWeapon weapon, 
OnWeaponSwingHitPoint | (Client) Fires when a local player's attack connects. | IsoPlayer attacker, HandWeapon weapon, 
OnWeatherPeriodComplete | (Server) Fires when a weather period finishes. | WeatherPeriod period, 
OnWeatherPeriodStage | (Server) Fires when a weather period progresses a stage. | WeatherPeriod period, 
OnWeatherPeriodStart | (Server) Fires when a weather period begins. | WeatherPeriod period, 
OnWeatherPeriodStop | (Server) Fires when a weather period ends early, such as by an admin command. | WeatherPeriod period, 
OnWorldMessage | (Deprecated)  | 
OnWorldSound | Fires whenever a world sound is created. | int x, int y, int z, int radius, int volume, Object source, 
OnZombieDead | (Client) Fires when a local zombie dies. The zombie's inventory is not filled with loot when this event fires, but their clothing and attached items are added. | IsoZombie zombie, 
OnZombieUpdate | (Client) Fires whenever a zombie updates. | IsoZombie zombie, 
preAddCatDefs | Fires before the foraging system processes item category definitions. | table system, 
preAddForageDefs | Fires before the foraging system processes any definitions. | table system, 
preAddItemDefs | Fires before the foraging system processes item definitions. | table system, 
preAddSkillDefs | Fires before the foraging system processes trait and profession definitions. | table system, 
preAddZoneDefs | Fires before the foraging system processes zone definitions. | table system, 
ReceiveFactionInvite | (Multiplayer) (Client) Fires when the client receives a faction invite. | String factionName, String hostUsername, 
ReceiveSafehouseInvite | (Multiplayer) (Client) Fires when the client receives a safehouse invite. | String title, String hostUsername, 
RequestTrade | (Multiplayer) (Client) Fires when the client receives a trade request. | String requester, 
ReuseGridsquare | Fires before a square is unloaded. | IsoGridSquare square, 
SendCustomModData | (Multiplayer) (Server) Fires when a client is requesting server moddata. | 
ServerPinged | (Multiplayer) (Client) Fires when receiving a ping response from the server. The 'numClients' string is suffixed with '/512'. | String clientAddress, String numClients, 
SwitchChatStream | (Multiplayer) (Client) Fires when the client switches chat tabs. | 
SyncFaction | (Multiplayer) (Client) Fires when the client receives changes to a faction. | String faction, 
TradingUIAddItem | (Multiplayer) (Client) Fires when the other player in a trade adds an item. | IsoPlayer player, InventoryItem item, 
TradingUIRemoveItem | (Multiplayer) (Client) Fires when the other player in a trade removes an item. | IsoPlayer player, int index, 
TradingUIUpdateState | (Multiplayer) (Client) Fires when the other player in a trade changes the state of the trade. | IsoPlayer player, int state, 
ViewTickets | (Multiplayer) (Client) Fires when receiving the list of tickets from the server. | ArrayList tickets, 

# Hooks
Hook | Description | Parameters
--- | --- | ---
Attack | (Client) Called every tick while a local character is pressing their attack button and is able to attack. | IsoLivingCharacter attacker, float chargeDelta, HandWeapon weapon, 
AutoDrink | (Client) Called whenever a character automatically drinks while auto-drink is turned on. | IsoGameCharacter character, 
CalculateStats | (Client) Called when a character's stats are being updated. Character health is not included. | IsoGameCharacter character, 
UseItem | (Deprecated)  | 
WeaponHitCharacter | Called when the effects of an attack are being calculated. | IsoGameCharacter attacker, IsoGameCharacter target, HandWeapon weapon, float damageSplit, 
WeaponSwing | Called when a weapon is swung to find targets | IsoGameCharacter character, HandWeapon weapon, 
WeaponSwingHitPoint | (Deprecated)  | 
