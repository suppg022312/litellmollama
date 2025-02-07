Creating a simple Expenses Claim application using Windows .NET MVC (Model-View-Controller) involves several steps. Since Windows doesn't traditionally use ASP.NET MVC, which is commonly associated with web applications, we'll adapt the concept to fit into a desktop application context.

Here's a basic outline for an expenses claim app using C# and WinForms (as MVC-like structure adapted for desktop), utilizing .NET Framework. Note that this won’t be pure MVC as traditionally understood but will follow similar principles of separating concerns.

**Step 1: Define Models**

First, let’s create our data models:

```csharp
public class ExpenseItem
{
    public int Id { get; set; }
    public string Description { get; set; }
    public decimal Amount { get; set; }
    public DateTime Date { get; set; }
}

public class ExpensesClaim
{
    public int Id { get; set; }
    public string ClaimantName { get; set; }
    public IEnumerable<ExpenseItem> Items { get; set; } = new List<ExpenseItem>();
}
```

**Step 2: Define Controllers**

For a desktop application, our "controller" logic would typically be in the form of managers or services handling data operations:

```csharp
public class ExpensesManager
{
    private static List<ExpensesClaim> _claims = new List<ExpensesClaim>();

    public void AddExpense(ExpenseItem item)
    {
        // Logic to add expense items to claims (e.g., finding the right claim based on current user, etc.)
    }

    public IEnumerable<ExpensesClaim> GetClaims()
    {
        return _claims;
    }
}
```

**Step 3: Define Views**

For WinForms, views are basically forms and dialogs:

```csharp
public partial class AddExpenseForm : Form
{
    private ExpensesManager _manager;

    public AddExpenseForm(ExpensesManager manager)
    {
        InitializeComponent();
        _manager = manager;
    }

    private void btnSave_Click(object sender, EventArgs e)
    {
        var item = new ExpenseItem
        {
            Description = txtDescription.Text,
            Amount = decimal.Parse(txtAmount.Text),
            Date = dtpDate.Value
        };
        _manager.AddExpense(item);
        this.Close(); // Close the form after saving.
    }
}
```

**Step 4: Putting It All Together**

Here’s how you might launch your app and interact with it:

```csharp
static class Program
{
    [STAThread]
    static void Main()
    {
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);

        var manager = new ExpensesManager();

        // Show the initial form to manage claims.
        var claimManagementForm = new ClaimsManagementForm(manager);
        Application.Run(claimManagementForm);
    }
}

public class ClaimsManagementForm : Form
{
    private ExpensesManager _manager;

    public ClaimsManagementForm(ExpensesManager manager)
    {
        InitializeComponent();
        _manager = manager;
        
        // Populate the form with existing claims.
        var claims = _manager.GetClaims();
        // Add UI logic to display these claims, e.g., DataGridView or custom controls.
    }

    private void btnAddExpense_Click(object sender, EventArgs e)
    {
        var addExpenseForm = new AddExpenseForm(_manager);
        addExpenseForm.Show();
    }
}
```

**Important Notes:**

- **MVC Misalignment**: This adaptation does not follow the exact MVC pattern due to WinForms' nature and limitations in desktop applications. It's more of a Model-View pattern with some rudimentary Controller-like logic.
- **Data Persistence**: For persistence, consider using databases (like SQL Server or SQLite) via ADO.NET or Entity Framework for more complex scenarios.
- **User Interaction**: The Views are handled through WinForms dialogs and forms which require manual UI creation (e.g., using `Form`, `DataGridView`).
- **Security & Authentication**: In a real application, you'd want to add user authentication and possibly role-based access control.

This structure provides a starting point for building an expenses claim app in C# with a desktop-oriented MVC-like pattern. Depending on your needs (like reporting, advanced data validation, etc.), you might need to expand upon this foundation.