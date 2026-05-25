# TMS - Transportation Management System (Web Version)

A responsive web-based Transportation Management System built with Flask. Access from your Android device, iPhone, Windows, Mac, or Linux!

## Features

✅ **Responsive Design** - Works perfectly on desktop, tablet, and mobile
✅ **Bus Management** - Add, view, and delete buses
✅ **Driver Management** - Manage driver information and licenses
✅ **Passenger Management** - Track passenger details
✅ **Ticket Management** - Handle ticket bookings and routes
✅ **SQLite Database** - All data persists locally
✅ **Real-time Updates** - Instant data refresh

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python web_app.py
```

You'll see output like:
```
Running on http://0.0.0.0:5000
```

### 3. Access from Your Android Device

On your Android phone/tablet:

**Option A: Direct Connection (Same WiFi)**
1. Find your computer's IP address:
   - Windows: Open Command Prompt and run `ipconfig`
   - Look for "IPv4 Address" (e.g., 192.168.x.x)
2. On your Android device, open a web browser
3. Enter: `http://<YOUR_COMPUTER_IP>:5000`

**Option B: USB Connection (if on same computer)**
- Simply go to: `http://localhost:5000`

## Usage

### Adding Data
1. Click on the relevant tab (Buses, Drivers, Passengers, Tickets)
2. Fill in the form fields
3. Click "Add [Item]" button
4. Data appears instantly below the form

### Viewing Data
- All entries automatically load when you switch to a tab
- Each entry shows all its details in a card format

### Deleting Data
- Click the "Delete" button on any entry
- Confirm deletion in the popup
- The item is removed instantly

## Supported Browsers
- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (Android Chrome, Firefox, Safari)

## Troubleshooting

**Can't connect from Android?**
- Make sure both devices are on the same WiFi network
- Check Windows Firewall - allow Python through firewall
- Verify you have the correct IP address

**Port 5000 already in use?**
- Edit `web_app.py` line 189: change `port=5000` to `port=5001` (or any unused port)

**Data not saving?**
- Check that .db files have write permissions
- Try running as Administrator

## Project Structure

```
TMS APP/
├── web_app.py              # Flask backend server
├── requirements.txt         # Python dependencies
├── templates/
│   └── index.html          # Main web interface
└── static/
    ├── style.css           # Responsive styling
    └── script.js           # Frontend JavaScript
```

## Database Files

The app creates these SQLite databases:
- `bus.db` - Bus information
- `drivers.db` - Driver details
- `passengers.db` - Passenger info
- `tickets.db` - Ticket records

## API Endpoints

- `GET /api/buses` - List all buses
- `POST /api/buses` - Add a bus
- `DELETE /api/buses/<id>` - Delete a bus

- `GET /api/drivers` - List all drivers
- `POST /api/drivers` - Add a driver
- `DELETE /api/drivers/<id>` - Delete a driver

- `GET /api/passengers` - List all passengers
- `POST /api/passengers` - Add a passenger
- `DELETE /api/passengers/<id>` - Delete a passenger

- `GET /api/tickets` - List all tickets
- `POST /api/tickets` - Add a ticket
- `DELETE /api/tickets/<id>` - Delete a ticket

## Notes

- Original CustomTkinter files (main.py, app.py, etc.) are still available
- To switch back to desktop version: `python main.py`
- Web version runs concurrently and doesn't conflict with desktop app
- All data is stored locally in SQLite database files

Enjoy your web-based TMS! 🚀
