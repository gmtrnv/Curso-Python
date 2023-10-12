#PALABRAS RESERVADAS EN PYTHON

<div class="content">
      <p>Keywords are the reserved words in Python. We cannot use a keyword as a variable name, function name or any other identifier.</p>

<p>Here's a list of all keywords in Python Programming</p>
<div class="table-responsive"><table border="0">
	<caption>Keywords in Python programming language</caption>
	<tbody>
		<tr>
			<td><a href="#true_false">False</a></td>
			<td><a href="#async_await">await</a></td>
			<td><a href="#if_else_elif">else</a></td>
			<td><a href="#from_import">import</a></td>
			<td><a href="#pass">pass</a></td>
		</tr>
		<tr>
			<td><a href="#none">None</a></td>
			<td><a href="#break_continue">break</a></td>
			<td><a href="#except_raise_try">except</a></td>
			<td><a href="#in">in</a></td>
			<td><a href="#except_raise_try">raise</a></td>
		</tr>
		<tr>
			<td><a href="#true_false">True</a></td>
			<td><a href="#class">class</a></td>
			<td><a href="#finally">finally</a></td>
			<td><a href="#is">is</a></td>
			<td><a href="#return">return</a></td>
		</tr>
		<tr>
			<td><a href="#and_or_not">and</a></td>
			<td><a href="#break_continue">continue</a></td>
			<td><a href="#for">for</a></td>
			<td><a href="#lambda">lambda</a></td>
			<td><a href="#except_raise_try">try</a></td>
		</tr>
		<tr>
			<td><a href="#as">as</a></td>
			<td><a href="#def">def</a></td>
			<td><a href="#from_import">from</a></td>
			<td><a href="#nonlocal">nonlocal</a></td>
			<td><a href="#while">while</a></td>
		</tr>
		<tr>
			<td><a href="#assert">assert</a></td>
			<td><a href="#del">del</a></td>
			<td><a href="#global">global</a></td>
			<td><a href="#and_or_not">not</a></td>
			<td><a href="#with">with</a></td>
		</tr>
		<tr>
			<td><a href="#asyn_await">async</a></td>
			<td><a href="#if_else_elif">elif</a></td>
			<td><a href="#if_else_elif">if</a></td>
			<td><a href="#and_or_not">or</a></td>
			<td><a href="#yield">yield</a></td>
		</tr>
	</tbody>
</table></div>

<p>The above keywords may get altered in different versions of Python. Some extra might get added or some might be removed. You can always get the list of keywords in your current version by typing the following in the prompt.</p>

<pre style="max-height: 600px;"><code class="python hljs">
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-keyword">import</span> keyword
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-keyword">print</span>(keyword.kwlist)
[<span class="hljs-string">'False'</span>, <span class="hljs-string">'None'</span>, <span class="hljs-string">'True'</span>, <span class="hljs-string">'and'</span>, <span class="hljs-string">'as'</span>, <span class="hljs-string">'assert'</span>, <span class="hljs-string">'async'</span>, <span class="hljs-string">'await'</span>, <span class="hljs-string">'break'</span>, <span class="hljs-string">'class'</span>, <span class="hljs-string">'continue'</span>, <span class="hljs-string">'def'</span>, <span class="hljs-string">'del'</span>, <span class="hljs-string">'elif'</span>, <span class="hljs-string">'else'</span>, <span class="hljs-string">'except'</span>, <span class="hljs-string">'finally'</span>, <span class="hljs-string">'for'</span>, <span class="hljs-string">'from'</span>, <span class="hljs-string">'global'</span>, <span class="hljs-string">'if'</span>, <span class="hljs-string">'import'</span>, <span class="hljs-string">'in'</span>, <span class="hljs-string">'is'</span>, <span class="hljs-string">'lambda'</span>, <span class="hljs-string">'nonlocal'</span>, <span class="hljs-string">'not'</span>, <span class="hljs-string">'or'</span>, <span class="hljs-string">'pass'</span>, <span class="hljs-string">'raise'</span>, <span class="hljs-string">'return'</span>, <span class="hljs-string">'try'</span>, <span class="hljs-string">'while'</span>, <span class="hljs-string">'with'</span>, <span class="hljs-string">'yield'</span>]
</code></pre>

<h2>Description of Keywords in Python with examples</h2>

<h3 id="true_false">True, False</h3>

<p><code>True</code> and <code>False</code> are truth values in Python. They are the results of comparison operations or logical (Boolean) operations in Python. For example:</p>

<pre style="max-height: 600px;"><code class="python hljs">
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-number">1</span> == <span class="hljs-number">1</span>
<span class="hljs-literal">True</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-number">5</span> &gt; <span class="hljs-number">3</span>
<span class="hljs-literal">True</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-literal">True</span> <span class="hljs-keyword">or</span> <span class="hljs-literal">False</span>
<span class="hljs-literal">True</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-number">10</span> &lt;= <span class="hljs-number">1</span>
<span class="hljs-literal">False</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-number">3</span> &gt; <span class="hljs-number">7</span>
<span class="hljs-literal">False</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-literal">True</span> <span class="hljs-keyword">and</span> <span class="hljs-literal">False</span>
<span class="hljs-literal">False</span>
</code></pre>  

<p>Here we can see that the first three statements are true so the interpreter returns <code>True</code> and returns <code>False</code> for the remaining three statements. <code>True</code> and <code>False</code> in python is same as <code>1</code> and <code>0</code>. This can be justified with the following example:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-literal">True</span> == <span class="hljs-number">1</span>
<span class="hljs-literal">True</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-literal">False</span> == <span class="hljs-number">0</span>
<span class="hljs-literal">True</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-literal">True</span> + <span class="hljs-literal">True</span>
<span class="hljs-number">2</span>
</code></pre>

<h3 id="none">None</h3>

<p><code>None</code> is a special constant in Python that represents the absence of a value or a null value.</p>

<p>It is an object of its own datatype, the <code>NoneType</code>. We cannot create multiple <code>None</code> objects but can assign it to variables. These variables will be equal to one another.</p>

<p>We must take special care that <code>None</code> does not imply <code>False</code>, <code>0</code> or any empty list, dictionary, string etc. For example:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-literal">None</span> == <span class="hljs-number">0</span>
<span class="hljs-literal">False</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-literal">None</span> == []
<span class="hljs-literal">False</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-literal">None</span> == <span class="hljs-literal">False</span>
<span class="hljs-literal">False</span>
<span class="hljs-meta">&gt;&gt;&gt; </span>x = <span class="hljs-literal">None</span>
<span class="hljs-meta">&gt;&gt;&gt; </span>y = <span class="hljs-literal">None</span>
<span class="hljs-meta">&gt;&gt;&gt; </span>x == y
<span class="hljs-literal">True</span>
</code></pre>

<p>Void functions that do not return anything will return a <code>None</code> object automatically. <code>None</code> is also returned by functions in which the program flow does not encounter a return statement. For example:</p>

<pre style="max-height: 600px;"><code class="python hljs">
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">a_void_function</span><span class="hljs-params">()</span>:</span>
    a = <span class="hljs-number">1</span>
    b = <span class="hljs-number">2</span>
    c = a + b

x = a_void_function()
<span class="hljs-keyword">print</span>(x)
</code></pre>

<p><b>Output</b></p>

<pre><samp>
None
</samp></pre>

<p>This program has a function that does not return a value, although it does some operations inside. So when we print <var>x</var>, we get <code>None</code> which is returned automatically (implicitly). Similarly, here is another example:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">improper_return_function</span><span class="hljs-params">(a)</span>:</span>
    <span class="hljs-keyword">if</span> (a % <span class="hljs-number">2</span>) == <span class="hljs-number">0</span>:
        <span class="hljs-keyword">return</span> <span class="hljs-literal">True</span>

x = improper_return_function(<span class="hljs-number">3</span>)
<span class="hljs-keyword">print</span>(x)
</code></pre>

<p><b>Output</b></p>

<pre><samp>None
</samp></pre>

<p>Although this function has a <code>return</code> statement, it is not reached in every case. The function will return <code>True</code> only when the input is even.</p>

<p>If we give the function an odd number, <code>None</code> is returned implicitly.</p>

<h3 id="and_or_not">and, or , not</h3>

<p><code>and</code>, <code>or</code>, <code>not</code> are the logical operators in Python. <code>and</code> will result into <code>True</code> only if both the operands are <code>True</code>. The truth table for <code>and</code> is given below:</p>

<div class="table-responsive"><table border="0">
	<caption>Truth table for <code>and</code></caption>
	<tbody>
		<tr>
			<th scope="col">A</th>
			<th scope="col">B</th>
			<th scope="col">A and B</th>
		</tr>
		<tr>
			<td>True</td>
			<td>True</td>
			<td>True</td>
		</tr>
		<tr>
			<td>True</td>
			<td>False</td>
			<td>False</td>
		</tr>
		<tr>
			<td>False</td>
			<td>True</td>
			<td>False</td>
		</tr>
		<tr>
			<td>False</td>
			<td>False</td>
			<td>False</td>
		</tr>
	</tbody>
</table></div>

<p><code>or</code> will result into <code>True</code> if any of the operands is <code>True</code>. The truth table for <code>or</code> is given below:</p>

<div class="table-responsive"><table border="0">
	<caption>Truth table for <code>or</code></caption>
	<tbody>
		<tr>
			<th scope="col">A</th>
			<th scope="col">B</th>
			<th scope="col">A or B</th>
		</tr>
		<tr>
			<td>True</td>
			<td>True</td>
			<td>True</td>
		</tr>
		<tr>
			<td>True</td>
			<td>False</td>
			<td>True</td>
		</tr>
		<tr>
			<td>False</td>
			<td>True</td>
			<td>True</td>
		</tr>
		<tr>
			<td>False</td>
			<td>False</td>
			<td>False</td>
		</tr>
	</tbody>
</table></div>

<p><code>not</code> operator is used to invert the truth value. The truth table for <code>not</code> is given below:</p>

<div class="table-responsive"><table border="0">
	<caption>Truth tabel for <code>not</code></caption>
	<tbody>
		<tr>
			<th scope="col">A</th>
			<th scope="col">not A</th>
		</tr>
		<tr>
			<td>True</td>
			<td>False</td>
		</tr>
		<tr>
			<td>False</td>
			<td>True</td>
		</tr>
	</tbody>
</table></div>

<p>some example of their usage are given below</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-literal">True</span> <span class="hljs-keyword">and</span> <span class="hljs-literal">False</span>
<span class="hljs-literal">False</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-literal">True</span> <span class="hljs-keyword">or</span> <span class="hljs-literal">False</span>
<span class="hljs-literal">True</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-keyword">not</span> <span class="hljs-literal">False</span>
<span class="hljs-literal">True</span>
</code></pre>

<h3 id="as">as</h3>

<p><code>as</code> is used to create an alias while importing a module. It means giving a different name (user-defined) to a module while importing it.</p>

<p>As for example, Python has a standard module called <code>math</code>. Suppose we want to calculate what cosine pi is using an alias. We can do it as follows using <code>as</code>:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-keyword">import</span> math <span class="hljs-keyword">as</span> myAlias
&gt;&gt;&gt;myAlias.cos(myAlias.pi)
<span class="hljs-number">-1.0</span>
</code></pre>

<p>Here we imported the <code>math</code> module by giving it the name <code>myAlias</code>. Now we can refer to the <code>math</code> module with this name. Using this name we calculated cos(pi) and got <code>-1.0</code> as the answer.</p>

<h3 id="assert">assert</h3>

<p><code>assert</code> is used for debugging purposes.</p>

<p>While programming, sometimes we wish to know the internal state or check if our assumptions are true. <code>assert</code> helps us do this and find bugs more conveniently. <code>assert</code> is followed by a condition.</p>

<p>If the condition is true, nothing happens. But if the condition is false, <code>AssertionError</code> is raised. For example:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span>a = <span class="hljs-number">4</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-keyword">assert</span> a &lt; <span class="hljs-number">5</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-keyword">assert</span> a &gt; <span class="hljs-number">5</span>
Traceback (most recent call last):
  File <span class="hljs-string">"&lt;string&gt;"</span>, line <span class="hljs-number">301</span>, <span class="hljs-keyword">in</span> runcode
  File <span class="hljs-string">"&lt;interactive input&gt;"</span>, line <span class="hljs-number">1</span>, <span class="hljs-keyword">in</span> &lt;module&gt;
AssertionError
</code></pre>

<p>For our better understanding, we can also provide a message to be printed with the <code>AssertionError</code>.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span>a = <span class="hljs-number">4</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-keyword">assert</span> a &gt; <span class="hljs-number">5</span>, <span class="hljs-string">"The value of a is too small"</span>
Traceback (most recent call last):
  File <span class="hljs-string">"&lt;string&gt;"</span>, line <span class="hljs-number">301</span>, <span class="hljs-keyword">in</span> runcode
  File <span class="hljs-string">"&lt;interactive input&gt;"</span>, line <span class="hljs-number">1</span>, <span class="hljs-keyword">in</span> &lt;module&gt;
AssertionError: The value of a <span class="hljs-keyword">is</span> too small
</code></pre>

<p>At this point we can note that,</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-keyword">assert</span> condition, message
</code></pre>

<p>is equivalent to,</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> condition:
    <span class="hljs-keyword">raise</span> AssertionError(message)</code></pre>

<h3 id="async_await">async, await</h3>

<p>The <code>async</code> and <code>await</code> keywords are provided by the <code>asyncio</code> library in Python. They are used to write concurrent code in Python. For example,</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-keyword">import</span> asyncio

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">main</span><span class="hljs-params">()</span>:</span>
    <span class="hljs-keyword">print</span>(<span class="hljs-string">'Hello'</span>)
    <span class="hljs-keyword">await</span> asyncio.sleep(<span class="hljs-number">1</span>)
    <span class="hljs-keyword">print</span>(<span class="hljs-string">'world'</span>)</code></pre>

<p>To run the program, we use</p>

<pre style="max-height: 600px;"><code class="python hljs">asyncio.run(main())</code></pre>

<p>In the above program, the <code>async</code> keyword specifies that the function will be executed asynchronously.</p>

<p>Here, first <var>Hello</var> is printed. The <code>await</code> keyword makes the program wait for 1 second. And then the <var>world</var> is printed.</p>

<h3 id="break_continue">break, continue</h3>

<p><code>break</code> and <code>continue</code> are used inside <code>for</code> and <code>while</code> loops to alter their normal behavior.</p>

<p><code>break</code> will end the smallest loop it is in and control flows to the statement immediately below the loop. <code>continue</code> causes to end the current iteration of the loop, but not the whole loop.</p>

<p>This can be illustrated with the following two examples:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(<span class="hljs-number">1</span>,<span class="hljs-number">11</span>):
    <span class="hljs-keyword">if</span> i == <span class="hljs-number">5</span>:
        <span class="hljs-keyword">break</span>
    <span class="hljs-keyword">print</span>(i)
</code></pre>

<p><b>Output</b></p>

<pre><samp>1
2
3
4
</samp></pre>

<p>Here, the <code>for</code> loop intends to print numbers from 1 to 10. But the <code>if</code> condition is met when <var>i</var> is equal to 5 and we break from the loop. Thus, only the range 1 to 4 is printed.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(<span class="hljs-number">1</span>,<span class="hljs-number">11</span>):
    <span class="hljs-keyword">if</span> i == <span class="hljs-number">5</span>:
        <span class="hljs-keyword">continue</span>
    <span class="hljs-keyword">print</span>(i)
</code></pre>

<p><b>Output</b></p>

<pre><samp>1
2
3
4
6
7
8
9
10
</samp></pre>

<p>Here we use <code>continue</code> for the same program. So, when the condition is met, that iteration is skipped. But we do not exit the loop. Hence, all the values except 5 are printed out.</p>

<p>Learn more about <a href="/python-programming/break-continue" title="Python break and continue statement">Python break and continue statement</a>.</p>

<h3 id="class">class</h3>

<p><code>class</code> is used to define a new user-defined class in Python.</p>

<p>Class is a collection of related attributes and methods that try to represent a real-world situation. This idea of putting data and functions together in a class is central to the concept of object-oriented programming (OOP).</p>

<p>Classes can be defined anywhere in a program. But it is a good practice to define a single class in a module. Following is a sample usage:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ExampleClass</span>:</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">function1</span><span class="hljs-params">(parameters)</span>:</span>
        …
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">function2</span><span class="hljs-params">(parameters)</span>:</span>
        …
</code></pre>

<p>Learn more about <a href="/python-programming/class" title="Python Objects and Class">Python Objects and Class</a>.</p>

<h3 id="def">def</h3>

<p><code>def</code> is used to define a user-defined function.</p>

<p>Function is a block of related statements, which together does some specific task. It helps us organize code into manageable chunks and also to do some repetitive task.</p>

<p>The usage of <code>def</code> is shown below:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">function_name</span><span class="hljs-params">(parameters)</span>:</span>
    …
</code></pre>

<p>Learn more about <a href="/python-programming/function" title="Python Functions">Python functions</a>.</p>

<h3 id="del">del</h3>

<p><code>del</code> is used to delete the reference to an object. Everything is object in Python. We can delete a variable reference using <code>del</code></p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span>a = b = <span class="hljs-number">5</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-keyword">del</span> a
<span class="hljs-meta">&gt;&gt;&gt; </span>a
Traceback (most recent call last):
  File <span class="hljs-string">"&lt;string&gt;"</span>, line <span class="hljs-number">301</span>, <span class="hljs-keyword">in</span> runcode
  File <span class="hljs-string">"&lt;interactive input&gt;"</span>, line <span class="hljs-number">1</span>, <span class="hljs-keyword">in</span> &lt;module&gt;
NameError: name <span class="hljs-string">'a'</span> <span class="hljs-keyword">is</span> <span class="hljs-keyword">not</span> defined
<span class="hljs-meta">&gt;&gt;&gt; </span>b
<span class="hljs-number">5</span>
</code></pre>

<p>Here we can see that the reference of the variable <var>a</var> was deleted. So, it is no longer defined. But <var>b</var> still exists.</p>

<p><code>del</code> is also used to delete items from a list or a dictionary:</p>

<pre style="max-height: 600px;"><code class="python hljs">
<span class="hljs-meta">&gt;&gt;&gt; </span>a = [<span class="hljs-string">'x'</span>,<span class="hljs-string">'y'</span>,<span class="hljs-string">'z'</span>]
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-keyword">del</span> a[<span class="hljs-number">1</span>]
<span class="hljs-meta">&gt;&gt;&gt; </span>a
[<span class="hljs-string">'x'</span>, <span class="hljs-string">'z'</span>]
</code></pre>

<h3 id="if_else_elif">if, else, elif</h3>

<p><code>if, else, elif</code> are used for conditional branching or decision making.</p>

<p>When we want to test some condition and execute a block only if the condition is true, then we use <code>if</code> and <code>elif</code>. <code>elif</code> is short for else if. <code>else</code> is the block which is executed if the condition is false. This will be clear with the following example:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">if_example</span><span class="hljs-params">(a)</span>:</span>
    <span class="hljs-keyword">if</span> a == <span class="hljs-number">1</span>:
        <span class="hljs-keyword">print</span>(<span class="hljs-string">'One'</span>)
    <span class="hljs-keyword">elif</span> a == <span class="hljs-number">2</span>:
        <span class="hljs-keyword">print</span>(<span class="hljs-string">'Two'</span>)
    <span class="hljs-keyword">else</span>:
        <span class="hljs-keyword">print</span>(<span class="hljs-string">'Something else'</span>)

if_example(<span class="hljs-number">2</span>)
if_example(<span class="hljs-number">4</span>)
if_example(<span class="hljs-number">1</span>)
</code></pre>

<p><b>Output</b></p>

<pre><samp>Two
Something else
One
</samp></pre>

<p>Here, the function checks the input number and prints the result if it is 1 or 2. Any input other than this will cause the <code>else</code> part of the code to execute.</p>

<p>Learn more about <a href="/python-programming/if-elif-else" title="Python if Statement">Python if and if...else Statement</a>.</p>

<h3 id="except_raise_try">except, raise, try</h3>

<p><code>except, raise, try</code> are used with exceptions in Python.</p>

<p>Exceptions are basically errors that suggests something went wrong while executing our program. <code>IOError</code>, <code>ValueError</code>, <code>ZeroDivisionError</code>, <code>ImportError</code>, <code>NameError</code>, <code>TypeError</code> etc. are few examples of exception in Python. <code>try...except</code> blocks are used to catch exceptions in Python.</p>

<p>We can raise an exception explicitly with the <code>raise</code> keyword. Following is an example:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">reciprocal</span><span class="hljs-params">(num)</span>:</span>
    <span class="hljs-keyword">try</span>:
        r = <span class="hljs-number">1</span>/num
    <span class="hljs-keyword">except</span>:
        <span class="hljs-keyword">print</span>(<span class="hljs-string">'Exception caught'</span>)
        <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">return</span> r

<span class="hljs-keyword">print</span>(reciprocal(<span class="hljs-number">10</span>))
<span class="hljs-keyword">print</span>(reciprocal(<span class="hljs-number">0</span>))
</code></pre>

<p><b>Output</b></p>

<pre><samp>0.1
Exception caught
None
</samp></pre>

<p>Here, the function <code>reciprocal()</code> returns the reciprocal of the input number.</p>

<p>When we enter 10, we get the normal output of 0.1. But when we input 0, a <code>ZeroDivisionError</code> is raised automatically.</p>

<p>This is caught by our <code>try…except</code> block and we return <code>None</code>. We could have also raised the <code>ZeroDivisionError</code> explicitly by checking the input and handled it elsewhere as follows:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-keyword">if</span> num == <span class="hljs-number">0</span>:
    <span class="hljs-keyword">raise</span> ZeroDivisionError(<span class="hljs-string">'cannot divide'</span>)
</code></pre>

<h3 id="finally">finally</h3>

<p><code>finally</code> is used with <code>try…except</code> block to close up resources or file streams.</p>

<p>Using <code>finally</code> ensures that the block of code inside it gets executed even if there is an unhandled exception. For example:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-keyword">try</span>:
    Try-block
<span class="hljs-keyword">except</span> exception1:
    Exception1-block
<span class="hljs-keyword">except</span> exception2:
    Exception2-block
<span class="hljs-keyword">else</span>:
    Else-block
<span class="hljs-keyword">finally</span>:
    Finally-block
</code></pre>

<p>Here if there is an exception in the <code>Try-block</code>, it is handled in the <code>except</code> or <code>else</code> block. But no matter in what order the execution flows, we can rest assured that the <code>Finally-block</code> is executed even if there is an error. This is useful in cleaning up the resources.</p>

<p>Learn more about <a href="/python-programming/exception-handling" title="Python Exception Handling">exception handling in Python programming</a>.</p>

<h3 id="for">for</h3>

<p><code>for</code> is used for looping. Generally we use <code>for</code> when we know the number of times we want to loop.</p>

<p>In Python we can use it with any type of sequences like a list or a string. Here is an example in which <code>for</code> is used to traverse through a list of names:</p>

<pre style="max-height: 600px;"><code class="python hljs">names = [<span class="hljs-string">'John'</span>,<span class="hljs-string">'Monica'</span>,<span class="hljs-string">'Steven'</span>,<span class="hljs-string">'Robin'</span>]
<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> names:
    <span class="hljs-keyword">print</span>(<span class="hljs-string">'Hello '</span>+i)
</code></pre>

<p><b>Output</b></p>

<pre><samp>Hello John
Hello Monica
Hello Steven
Hello Robin
</samp></pre>

<p>Learn more about <a href="/python-programming/for-loop" title="Python for Loop">Python for loop</a>.</p>

<h3 id="from_import">from, import</h3>

<p><code>import</code> keyword is used to import modules into the current namespace. <code>from…import</code> is used to import specific attributes or functions into the current namespace. For example:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-keyword">import</span> math
</code></pre>

<p>will import the <code>math</code> module. Now we can use the <code>cos()</code> function inside it as <code>math.cos()</code>. But if we wanted to import just the <code>cos()</code> function, this can done using <code>from</code> as</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-keyword">from</span> math <span class="hljs-keyword">import</span> cos
</code></pre>

<p>now we can use the function simply as <code>cos()</code>, no need to write <code>math.cos()</code>.</p>

<p>Learn more on <a href="/python-programming/modules" title="Python Modules">Python modules and import statement</a>.</p>

<h3 id="global">global</h3>

<p><code>global</code> is used to declare that a variable inside the function is global (outside the function).</p>

<p>If we need to read the value of a global variable, it is not necessary to define it as <code>global</code>. This is understood.</p>

<p>If we need to modify the value of a global variable inside a function, then we must declare it with <code>global</code>. Otherwise, a local variable with that name is created.</p>

<p>Following example will help us clarify this.</p>

<pre style="max-height: 600px;"><code class="python hljs">globvar = <span class="hljs-number">10</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">read1</span><span class="hljs-params">()</span>:</span>
    <span class="hljs-keyword">print</span>(globvar)
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">write1</span><span class="hljs-params">()</span>:</span>
    <span class="hljs-keyword">global</span> globvar
    globvar = <span class="hljs-number">5</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">write2</span><span class="hljs-params">()</span>:</span>
    globvar = <span class="hljs-number">15</span>

read1()
write1()
read1()
write2()
read1()
</code></pre>

<p><b>Output</b></p>

<pre><samp>10
5
5
</samp></pre>

<p>Here, the <code>read1()</code> function is just reading the value of <code>globvar</code>. So, we do not need to declare it as <code>global</code>. But the <code>write1()</code> function is modifying the value, so we need to declare the variable as <code>global</code>.</p>

<p>We can see in our output that the modification did take place (10 is changed to 5). The <code>write2()</code> also tries to modify this value. But we have not declared it as <code>global</code>.</p>

<p>Hence, a new local variable <code>globvar</code> is created which is not visible outside this function. Although we modify this local variable to 15, the global variable remains unchanged. This is clearly visible in our output.</p>

<h3 id="in">in</h3>

<p><code>in</code> is used to test if a sequence (list, tuple, string etc.) contains a value. It returns <code>True</code> if the value is present, else it returns <code>False</code>. For example:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span>a = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>]
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-number">5</span> <span class="hljs-keyword">in</span> a
<span class="hljs-literal">True</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-number">10</span> <span class="hljs-keyword">in</span> a
<span class="hljs-literal">False</span>
</code></pre>

<p>The secondary use of <code>in</code> is to traverse through a sequence in a <code>for</code> loop.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-string">'hello'</span>:
    <span class="hljs-keyword">print</span>(i)
</code></pre>

<p><b>Output</b></p>

<pre><samp>h
e
l
l
o
</samp></pre>

<h3 id="is">is</h3>

<p><code>is</code> is used in Python for testing object identity. While the <code>==</code> operator is used to test if two variables are equal or not, <code>is</code> is used to test if the two variables refer to the same object.</p>

<p>It returns <code>True</code> if the objects are identical and <code>False</code> if not.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-literal">True</span> <span class="hljs-keyword">is</span> <span class="hljs-literal">True</span>
<span class="hljs-literal">True</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-literal">False</span> <span class="hljs-keyword">is</span> <span class="hljs-literal">False</span>
<span class="hljs-literal">True</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-literal">None</span> <span class="hljs-keyword">is</span> <span class="hljs-literal">None</span>
<span class="hljs-literal">True</span>
</code></pre>

<p>We know that there is only one instance of <code>True</code>, <code>False</code> and <code>None</code> in Python, so they are identical.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span>[] == []
<span class="hljs-literal">True</span>
<span class="hljs-meta">&gt;&gt;&gt; </span>[] <span class="hljs-keyword">is</span> []
<span class="hljs-literal">False</span>
<span class="hljs-meta">&gt;&gt;&gt; </span>{} == {}
<span class="hljs-literal">True</span>
<span class="hljs-meta">&gt;&gt;&gt; </span>{} <span class="hljs-keyword">is</span> {}
<span class="hljs-literal">False</span>
</code></pre>

<p>An empty list or dictionary is equal to another empty one. But they are not identical objects as they are located separately in memory. This is because list and dictionary are mutable (value can be changed).</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-string">''</span> == <span class="hljs-string">''</span>
<span class="hljs-literal">True</span>
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-string">''</span> <span class="hljs-keyword">is</span> <span class="hljs-string">''</span>
<span class="hljs-literal">True</span>
<span class="hljs-meta">&gt;&gt;&gt; </span>() == ()
<span class="hljs-literal">True</span>
<span class="hljs-meta">&gt;&gt;&gt; </span>() <span class="hljs-keyword">is</span> ()
<span class="hljs-literal">True</span>
</code></pre>

<p>Unlike list and dictionary, string and tuple are immutable (value cannot be altered once defined). Hence, two equal string or tuple are identical as well. They refer to the same memory location.</p>

<h3 id="lambda">lambda</h3>

<p><code>lambda</code> is used to create an anonymous function (function with no name). It is an inline function that does not contain a <code>return</code> statement. It consists of an expression that is evaluated and returned. For example:</p>

<pre style="max-height: 600px;"><code class="python hljs">a = <span class="hljs-keyword">lambda</span> x: x*<span class="hljs-number">2</span>
<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(<span class="hljs-number">1</span>,<span class="hljs-number">6</span>):
    <span class="hljs-keyword">print</span>(a(i))
</code></pre>

<p><b>Output</b></p>

<pre><samp>2
4
6
8
10
</samp></pre>

<p>Here, we have created an inline function that doubles the value, using the <code>lambda</code> statement. We used this to double the values in a list containing 1 to 5.</p>

<p>Learn more about <a href="/python-programming/anonymous-function" title="Python lamda function">Python lamda function</a>.</p>

<h3 id="nonlocal">nonlocal</h3>

<p>The use of <code>nonlocal</code> keyword is very much similar to the <code>global</code> keyword. <code>nonlocal</code> is used to declare that a variable inside a nested function (function inside a function) is not local to it, meaning it lies in the outer inclosing function. If we need to modify the value of a non-local variable inside a nested function, then we must declare it with <code>nonlocal</code>. Otherwise a local variable with that name is created inside the nested function. Following example will help us clarify this.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">outer_function</span><span class="hljs-params">()</span>:</span>
    a = <span class="hljs-number">5</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">inner_function</span><span class="hljs-params">()</span>:</span>
        <span class="hljs-keyword">nonlocal</span> a
        a = <span class="hljs-number">10</span>
        <span class="hljs-keyword">print</span>(<span class="hljs-string">"Inner function: "</span>,a)
    inner_function()
    <span class="hljs-keyword">print</span>(<span class="hljs-string">"Outer function: "</span>,a)

outer_function()
</code></pre>

<p><b>Output</b></p>

<pre><samp>Inner function:  10
Outer function:  10
</samp></pre>

<p>Here, the <code>inner_function()</code> is nested within the <code>outer_function</code>.</p>

<p>The variable <var>a</var> is in the <code>outer_function()</code>. So, if we want to modify it in the <code>inner_function()</code>, we must declare it as <code>nonlocal</code>. Notice that <var>a</var> is not a global variable.</p>

<p>Hence, we see from the output that the variable was successfully modified inside the nested <code>inner_function()</code>. The result of not using the <code>nonlocal</code> keyword is as follows:</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">outer_function</span><span class="hljs-params">()</span>:</span>
    a = <span class="hljs-number">5</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">inner_function</span><span class="hljs-params">()</span>:</span>
        a = <span class="hljs-number">10</span>
        <span class="hljs-keyword">print</span>(<span class="hljs-string">"Inner function: "</span>,a)
    inner_function()
    <span class="hljs-keyword">print</span>(<span class="hljs-string">"Outer function: "</span>,a)

outer_function()
</code></pre>

<p><b>Output</b></p>

<pre><samp>Inner function:  10
Outer function:  5
</samp></pre>

<p>Here, we do not declare that the variable <var>a</var> inside the nested function is <code>nonlocal</code>. Hence, a new local variable with the same name is created, but the non-local <var>a</var> is not modified as seen in our output.</p>

<h3 id="pass">pass</h3>

<p><code>pass</code> is a null statement in Python. Nothing happens when it is executed. It is used as a placeholder.</p>

<p>Suppose we have a function that is not implemented yet, but we want to implement it in the future. Simply writing,</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">function</span><span class="hljs-params">(args)</span>:</span>
</code></pre>

<p>in the middle of a program will give us <code>IndentationError</code>. Instead of this, we construct a blank body with the <code>pass</code> statement.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">function</span><span class="hljs-params">(args)</span>:</span>
    <span class="hljs-keyword">pass</span>
</code></pre>

<p>We can do the same thing in an empty <code>class</code> as well.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">example</span>:</span>
    <span class="hljs-keyword">pass</span>
</code></pre>

<h3 id="return">return</h3>

<p><code>return</code> statement is used inside a function to exit it and return a value.</p>

<p>If we do not return a value explicitly, <code>None</code> is returned automatically. This is verified with the following example.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">func_return</span><span class="hljs-params">()</span>:</span>
    a = <span class="hljs-number">10</span>
    <span class="hljs-keyword">return</span> a

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">no_return</span><span class="hljs-params">()</span>:</span>
    a = <span class="hljs-number">10</span>

<span class="hljs-keyword">print</span>(func_return())
<span class="hljs-keyword">print</span>(no_return())
</code></pre>

<p><b>Output</b></p>

<pre><samp>10
None
</samp></pre>

<h3 id="while">while</h3>

<p><code>while</code> is used for looping in Python.</p>

<p>The statements inside a <code>while</code> loop continue to execute until the condition for the <code>while</code> loop evaluates to <code>False</code> or a <code>break</code> statement is encountered. Following program illustrates this.</p>

<pre style="max-height: 600px;"><code class="python hljs">i = <span class="hljs-number">5</span>
<span class="hljs-keyword">while</span>(i):
    <span class="hljs-keyword">print</span>(i)
    i = i – <span class="hljs-number">1</span>
</code></pre>

<p><b>Output</b></p>

<pre><samp>5
4
3
2
1
</samp></pre>

<p>Note that 0 is equal to <code>False</code>.</p>

<p>Learn more about <a href="/python-programming/while-loop" title="Python for loop">Python while loop</a>.</p>

<h3 id="with">with</h3>

<p><code>with</code> statement is used to wrap the execution of a block of code within methods defined by the context manager.</p>

<p>Context manager is a class that implements <code>__enter__</code> and <code>__exit__</code> methods. Use of <code>with</code> statement ensures that the <code>__exit__</code> method is called at the end of the nested block. This concept is similar to the use of <code>try…finally</code> block. Here, is an example.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-keyword">with</span> open(<span class="hljs-string">'example.txt'</span>, <span class="hljs-string">'w'</span>) <span class="hljs-keyword">as</span> my_file:
    my_file.write(<span class="hljs-string">'Hello world!'</span>)
</code></pre>

<p>This example writes the text <code>Hello world!</code> to the file <code>example.txt</code>. File objects have <code>__enter__</code> and <code>__exit__</code> method defined within them, so they act as their own context manager.</p>

<p>First the <code>__enter__</code> method is called, then the code within <code>with</code> statement is executed and finally the <code>__exit__</code> method is called. <code>__exit__</code> method is called even if there is an error. It basically closes the file stream.</p>

<h3 id="yield">yield</h3>

<p><code>yield</code> is used inside a function like a <code>return</code> statement. But <code>yield</code> returns a generator.</p>

<p>Generator is an iterator that generates one item at a time. A large list of values will take up a lot of memory. Generators are useful in this situation as it generates only one value at a time instead of storing all the values in memory. For example,</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span>g = (<span class="hljs-number">2</span>**x <span class="hljs-keyword">for</span> x <span class="hljs-keyword">in</span> range(<span class="hljs-number">100</span>))
</code></pre>

<p>will create a generator <var>g</var> which generates powers of 2 up to the number two raised to the power 99. We can generate the numbers using the <code>next()</code> function as shown below.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span>next(g)
<span class="hljs-number">1</span>
<span class="hljs-meta">&gt;&gt;&gt; </span>next(g)
<span class="hljs-number">2</span>
<span class="hljs-meta">&gt;&gt;&gt; </span>next(g)
<span class="hljs-number">4</span>
<span class="hljs-meta">&gt;&gt;&gt; </span>next(g)
<span class="hljs-number">8</span>
<span class="hljs-meta">&gt;&gt;&gt; </span>next(g)
<span class="hljs-number">16</span>
</code></pre>

<p>And so on… This type of generator is returned by the <code>yield</code> statement from a function. Here is an example.</p>

<pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">generator</span><span class="hljs-params">()</span>:</span>
    <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(<span class="hljs-number">6</span>):
        <span class="hljs-keyword">yield</span> i*i

g = generator()
<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> g:
    <span class="hljs-keyword">print</span>(i)
</code></pre>

<p><b>Output</b></p>

<pre><samp>0
1
4
9
16
25
</samp></pre>

<p>Here, the function <code>generator()</code> returns a generator that generates square of numbers from 0 to 5. This is printed in the <code>for</code> loop.</p>
  </div>